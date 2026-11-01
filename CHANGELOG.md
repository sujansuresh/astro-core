# CHANGELOG.md — Vijay Transit (Rahu–Ketu Gochara Report Generator)

> **Purpose**: the single end-to-end change record for this project — every session,
> file, decision, and gate-kept blocker, with date-time and heading detail.
> **Conventions**:
> - Entries newest-at-bottom within each date; dates as `YYYY-MM-DD`, times `HH:MM IST`
>   where known. (History before this file existed is date-level only; exact times
>   are recorded from 2026-10-31 10:33 IST onward.)
> **Rule-ID glossary**: master table in `rule-engine/RULES.md` → GLOSSARY; per-file subsets
> at the top of each `.md`.
> - **Statuses**: `OPEN` · `BLOCKING` (a downstream build step cannot start) ·
>   `RESOLVED` · `DEFERRED-v2` · `HELD` (a call was made; may be reopened).
> - **Gate-kept items** get a stable `GK-xx` ID in the registry below; session entries
>   reference them. Gate-kept = parked with an owner, never silently dropped.
> - Owners: **Machan** (project owner, practice rulings) · **Panduranga** (developer —
>   ephemeris/motion-math items) · **Claude** (KB/rule formalization work).
> - Mirror rule: session-level facts also land in `MEMORY.md`; GK items also live in
>   the footer of the file they block. This changelog is the consolidated view.

---

## 🚧 GATE-KEPT ITEMS REGISTRY (live — read this first)

| GK | Logged | Item | Owner | Status | Blocks |
|---|---|---|---|---|---|
| **GK-01** | 2026-10-31 10:33 IST | **Factor-D unit discrepancy**: AGENTS.md says "~40–41 days per nakshatra"; mean-node astronomy gives ≈252d/nakshatra, ≈63d/pada (0.05295°/day, 6,798d cycle, 566d/sign). 40–41d matches neither. Resolve: is 40–41d a practice convention, a true-node unit, or a typo? Details in `foundations/rahu-ketu.md` Part 1.1 flag. | **Panduranga** | **OPEN · BLOCKING** | Factor-D sub-period renderer; rahu-ketu.md → LOCKED |
| **GK-02** | 2026-10-30 | **Ayanamsha mismatch**: natal PDF = KP Old 23°39'03"; transit PDF = KP New 24°08'34"; AGENTS.md says "Lahiri". Recommendation on file: KP Old. | Machan | OPEN · BLOCKING | Any computed chart; byte-parity with "Astro Predictors" |
| **GK-03** | 2026-10-31 | **Vimshottari year-length**: 360d classical vs 365.25d civil + render rounding — must match what "Astro Predictors" prints. `foundations/vimshottari.md` convention note. **Now a measured debt**: engine prints bhukti boundaries ~2–12 d off the documented table (e.g., Moon bhukti end computed 2027-04-09 vs printed 2027-04-11). Constant `DASHA_YEAR_DAYS` is ready to flip; Panduranga sorts the residual drift after the print convention is confirmed. | Machan (confirm print) → **Panduranga (debt: close residual drift)** | OPEN · BLOCKING | Byte-parity of dasha dates; vimshottari.md → LOCKED |
| **GK-04** | 2026-10-31 | **Moolam pada discrepancy**: natal PDF prints Rahu Dhanus 12°53' = Moolam **pada 1**; standard pada math = **pada 4**. Files currently follow the PDF. | Machan | OPEN | grahas.md/nakshatras.md Rahu entries → LOCKED |
| **GK-05** | 2026-10-30 | **R8 — remarriage bhava set** {8,11,7} flagged for ruling. | Machan | OPEN | kelvigal.md R8 card → LOCKED; bhavas.md 2nd-house note |
| **GK-06** | 2026-10-30 | **Decision #6 — gender-conditional spouse karaka** (Venus male-chart / Jupiter female-chart). Gates 5 school notes in `uyir-porul.md`. | Machan | OPEN | uyir-porul.md + R-domain cards → LOCKED |
| **GK-07** | 2026-10-30 | **Decision #1 — final domain list**: parked candidates education / property / children / spirituality. | Machan | OPEN · BLOCKING | Wave 4: `domains.md` |
| **GK-08** | 2026-10-30 | **Decision #4 — report language**: Tamil / English / both. | Machan | OPEN · BLOCKING | Wave 4: template files |
| **GK-09** | 2026-10-30 | **Decisions #2/#3/#5/#7**: report shape (one domain vs overview+deep-dive) · input contract (birth data vs precomputed positions) · remedies appendix y/n · KP sub-lord layer v2 (recommended yes). | Machan | OPEN | v1 scope freeze |
| **GK-10** | 2026-10-31 | **School-note queue (KB-wide)** — parampara variants awaiting ruling: bhavas.md ×5 (3rd mild-dusthana · 2nd second-marriage-family · 7th foreign-residence · 10th father day-charts · maraka scope HELD ayus-only) · functional-nature.md ×3 (Kanni Saturn lean · Dhanus Moon N-vs-M · mixed-cell rendering) · vimshottari.md ×2 (R-3 friction rule · R-2 node-relation borrowing) · rahu-ketu.md ×3 (Guru-Chandala-by-transit naming · dignity-commentary print/omit · half-return framing) · rasis.md ×2 (node co-lordship · Moon MT range) · uyir-porul.md ×5 (collapse into GK-06) · grahas.md editorial near-duplicates ×6 pairs (keep/merge). | Machan | OPEN | each file → REVIEWED/LOCKED |
| **GK-11** | 2026-10-31 | **Eight foundations files at DRAFT** awaiting Machan's line-by-line practice corrections: kelvigal · grahas (audited+fixed) · nakshatras · rasis · bhavas · functional-nature · uyir-porul · vimshottari. (rahu-ketu.md = ninth, added 2026-10-31 wave 3.) | Machan | OPEN · BLOCKING | contact-rules module (factor B engine) start |
| **GK-12** | 2026-10-31 11:08 IST | **ORB-02 sign-border question**: for a natal planet in a sign's last 3°, the applying phase begins *before* the node enters the sign (sample-chart Moon at 28°12': rise starts ≈ 2026-11-14, ≈23 days before the 2026-12-07 Makaram ingress). Ruling needed: does contact influence respect the sign boundary, or does the rise read from the border-crossing date? | Machan / Panduranga | **RESOLVED 2026-10-31** — Machan ruled: the curve is **sign-boundary independent**; influence may begin before ingress (early-influence register). Locked as ORB-02 clause | ORB-02 edge-case rendering; contact-window date renderer |
| **GK-13** | 2026-10-31 (later) | **Transit graha position feed**: RKT-08 clause B (nakshatra lord's transit house, transit dignity, conjunctions/aspects) requires full transit planet positions across the window — the current transit JSON carries node positions only. Source and granularity (daily ephemeris vs window snapshot) to be decided. | Machan / Panduranga | OPEN | RKT-08 clause-B evaluation; transit JSON contract (touches GK-09) |

---

## 2026-10-30 — SESSION 1: Project founding, sample ingestion, rule engine locked

### 2026-10-30 — Project founded + core decisions locked
- Folder created: `/Users/sujans/Desktop/vijay transit`.
- Goal set: domain-specific Rahu–Ketu gochara report generator — **logic first, code second**.
- 🔒 Locked (full table in AGENTS.md): mean node reported (true computed alongside) ·
  ayanamsha recorded as "Lahiri" (→ superseded by GK-02) · full ~18-month sign-transit
  window with dated sub-periods · styled self-contained HTML output · axis-first framing ·
  qualitative bands with stated reasons (no fake numeric precision) · v1 factors = A+B+C+D+E;
  F Ashtakavarga deferred-v2; G Vedha and H node-dignity excluded with reasons.

### 2026-10-30 — Sample PDFs fully read (natal 82pp + transit 31pp)
- Sample natal chart captured (female, 1992-03-02 22:23 Dindigul, KP Old): Lagna Thulam
  17°51'; Moon Makaram 28°12' (Avittam p2); 4-planet Makaram stellium (Mars 16°43' ucha /
  Saturn 19°23' own / Venus 22°23' / Moon) — double mahapurusha (Ruchaka + Shasha);
  Rahu Dhanus 12°53' (Moolam — GK-04), Ketu Mithunam 12°53' (Ardra p2).
- Vimshottari skeleton: Jupiter MD → 2030-08-10; Moon bhukti → 2027-04-11;
  Rahu bhukti 2028-03-17 → 2030-08-10.
- Transit event: Rahu enters Makaram ≈ 2026-12-07 → axis 4/10 Lagna, 1/7 Moon.
- Style reference locked: "Astro Predictors" PDF conventions (band labels, period-flow
  cards, signification tables).
- ⚠️ GK-02 logged (ayanamsha mismatch).

### 2026-10-30 — Product reframe + no-AI lock
- Machan's reframe: report GENERATOR (user natal + domain pick → curated report), not one-off.
- Architecture: compute once (factors A–E fact table) → per-domain lens config → verdict →
  stitched HTML. New domain = new config, engine untouched.
- 🔒 **No AI/LLM at runtime** — 100% deterministic, byte-identical outputs.
- 7 decisions tabled for Machan (→ GK-06/07/08/09).

### 2026-10-30 — LISA module + rule dump #1
- LISA (Lagna Influence & Signification Analysis) introduced: functional nature by lagna
  lordship · signification-based delivery · influence modification.
- Machan's first 5 axioms dumped (occupancy-first delivery; star-lord chain; kendra =
  material/status; trikona = heart/meaning; dispositor modulates tenant).
- Method locked: rule dumps → formalized rule cards → discuss → lock. Every rule carries a
  worked sample-chart example.
- Neecha-bhanga decision point surfaced: simplified vs classical rule **flips the chart's
  Mercury verdict** ( seeded Q3).

### 2026-10-30 — Q1 RESOLVED: signification chain (SIGN-01..04)
- 🔒 Ranks: own occupancy @100 → star-lord occupancy @100 → star-lord's owned houses →
  own owned houses; **SIGN-04 tenant-suppression**: ownership delivery 100% empty / 30%
  tenanted (rank-3 generalization agreed in Q2).
- Jupiter computed as the reference chain: {11 @100, 4 @100, 1&8 @100, 3&6 @30}.

### 2026-10-30 — Q2 RESOLVED: methodology mix + GATE-01 + DIGN-01; RULES.md founded
- 🔒 80% parambariya Parashara / 20% KP (star-lord chain only; sub-lord gate → v2).
- 🔒 GATE-01: per-QUESTION kelvikkaana bavagangal (core + modifier + viruddha);
  DBAS × transit → POSITIVE / MIXED / NEGATIVE.
- 🔒 DIGN-01: dignity = status visibility (thagudhi), independent of event manifestation.
- `rule-engine/RULES.md` created with first locked cards + domain lens seed.

### 2026-10-30 — Q3 RESOLVED: NBR-01 chain-rescue hierarchy + QUAL-01
- Machan's empirical read of sample Mercury (struggle → elevation) attributed to Saturn
  chain-rescue (star-lord + 3rd special aspect) — both mechanics verified in-chart.
- 🔒 NBR-01: c1 full bhanga (dispositor exalted/own) → c2 chain-rescue → c3 classical
  kendra conditions at 30% weight, never the gate.
- 🔒 QUAL-01: star-lord injects delivery QUALITY (third axis beside SIGN/SIGN-04).

### 2026-10-30 — Q4 RESOLVED: BHAVA-01/02/03 (purushartha underlayer)
- 🔒 Kendra = material/status; trikona = heart/meaning; 1st dual-textured; purushartha
  tags fixed (dharma 1/5/9 · artha 2/6/10 · kama 3/7/11 · moksha 4/8/12).

### 2026-10-30 — Q5 RESOLVED + NBR-02 filed
- 🔒 Q5 = one-tier drop for strong-tenant/debilitated-dispositor (partial, never annihilation).
- 🔒 NBR-02 (Machan's rule): uyir→porul exchange on full bhanga, keyed on FUNCTIONAL nature;
  malefic branch = conversion (harm incapacitated, no cost).

### 2026-10-30 — Micro-confirms: FUNC-01, PARI-01, REPORT-01; founding rule set COMPLETE
- 🔒 FUNC-01 (functional-over-natural; converse suppression does NOT fire) · PARI-01
  (parivartana dormant in DBAS, live in gochara on cusp contact) · NBR-02 scope = c1+c2 ·
  which-uyir = question-dependent, boundary faculties never hard-coded · REPORT-01 tone
  (~80% positive; negatives ~20% probabilistic, "irukkalaam/nadakkalaam/gavanam" register).
- **16 locked rule cards**: SIGN-01..05, FUNC-01, GATE-01, DIGN-01, BHAVA-01..03,
  STRENGTH-01, NBR-01, NBR-02, QUAL-01, PARI-01, REPORT-01.

### 2026-10-30 — KB standard set + build reorder
- `foundations/` named (general-purpose encyclopedia standard: e.g., ~200 karakatvas/graha).
- 🔒 Reorder: questions→bhavas catalog (kelvigal.md) FIRST, encyclopedia after.

---

## 2026-10-31 — SESSION 2: Foundations build-out (waves 1–3) + changelog established

### 2026-10-31 — `foundations/kelvigal.md` COMPLETE (wave 1, file 1)
- 50 question cards (10 × 5 domains), each with kelvikkana bhavagangal + kelvikkana kaaraka
  graham + "how arrived" derivation; append-only flavor-modifier bhavas; viruddha mechanics
  (12th-from-H on primary core; adverse houses as core for negative questions; family
  rotation anchors 4/9/7/5/3/11).

### 2026-10-31 — `foundations/grahas.md` COMPLETE + audited + fixed (wave 1, file 2)
- 9 graha entries to standard (identity / FUNC-01 nature / texture / good-bad banks /
  ≥200 numbered karakatvas + per-domain question-specific layers / dignity map / aspects /
  worked example).
- Machan-mandated **parallel-agent audit** run → fixes applied same day: Ketu example axis
  correction (nodes 180° apart); Sun FUNC-01 branch correction; Moon chain attribution +
  POSITIVE scope-limit; 18 kelvigal mapping gaps closed; Saturn disease bank backfilled
  to 210; Rahu #87–89 recategorized.
- Footer logs: GK-04, GK-06 marker, editorial near-duplicates ×6 pairs (→ GK-10).

### 2026-10-31 — `foundations/nakshatras.md` COMPLETE, 27/27 stars, 1,237 lines (wave 1, file 3)
- Per-star template: data line / texture / good-bad banks / ~24 karakatvas / pada map /
  factor-D transit note / factor-E dasha note / worked example for all 9 sample-chart
  placements. Pada navamsas re-verified. Retrograde contact order encoded
  (Moon→Venus→Saturn→Mars); Avittam sign-border split flagged.

### 2026-10-31 — `foundations/rasis.md` COMPLETE, 12/12, 613 lines → **WAVE 1 DONE**
- Per-rasi template incl. dignity & lordship map; worked examples for all 8 sample-chart
  rasis. Deferrals logged: enmity directionality → functional-nature.md (wave 2);
  node co-lordship + Moon MT range → GK-10.

### 2026-10-31 — `foundations/bhavas.md` COMPLETE, 12/12, 1,248 lines (wave 2, file 1)
- Classification grid, viruddha cycle, axis pairs, bhavat-bhavam anchors; per-bhava deep
  entries with kelvigal reverse-index; computed findings logged (2nd/10th most-pulled;
  6th most viruddha-watched — 11 cards; 9th widest modifier footprint + doubles as career
  viruddha; no card's primary viruddha lands on 10th). 5 school notes → GK-10.

### 2026-10-31 — `foundations/functional-nature.md` COMPLETE, 309 lines (wave 2, file 2)
- F-1..F-8 derivation rules; full 12-lagna × 7-graha matrix (108 cells, all derived with
  rule cites; nodes by proxy); **naisargika friend/enemy matrix WITH DIRECTION** (4
  asymmetric pairs resolved — rasis.md deferral closed); engine rule: factor C reads
  dispositor→tenant (willingness) and tenant→dispositor (comfort) separately; sample-chart
  functional panel + live factor-C cross-read. 3 school notes → GK-10.

### 2026-10-31 — `foundations/uyir-porul.md` COMPLETE, 263 lines (wave 2, file 3)
- NBR-02 lookup: 9 graha UYIR/PORUL/BOUNDARY tables (bhava-tagged, weight-ordered);
  pick mechanic formalized (SIGN-chain ∩ question bhavas → steer vs background);
  malefic branch = CONVERSION (no cost table); boundary faculties policy-locked (never
  hard-coded cost); worked Mercury example across 5 domains. 5 spouse-karaka notes → GK-06.

### 2026-10-31 — `foundations/vimshottari.md` COMPLETE (wave 2, file 4) → **WAVE 2 DONE**
- 120y wheel; balance-of-dasha math; **consistency proof: all 3 locked bhukti dates
  (2027-04-11 / 2028-03-17 / 2030-08-10) reproduce from formula, zero-fudging**; 9 MD
  textures; MD×AD rules R-1..R-6; GATE-01 DBAS-leg formal spec (AD ≥100 bar, MD half-weight).
- ⛔ GK-03 logged (year-length convention, byte-parity).

### 2026-10-31 — `foundations/rahu-ketu.md` COMPLETE, 400 lines (wave 3)
- Part 0 doctrine: chaya graha; head/tail; shanivat-Rahu / kujavat-Ketu WITH LIMITS
  (texture-only borrowing); dignity commentary-only (H); aspects OFF (7th-from already
  covered by axis-first read — ON would double-count the partner house).
- Part 1 motion mechanics (mean-node): 6,798d cycle · 0.05295°/day · 566d/sign ·
  252d/nakshatra · 63d/pada; orb windows computed (±3° = 113d exact band; ±5° = 189d
  active zone → stellium contacts overlap → dated peaks inside overlapping bands);
  retrograde = reverse-degree contact order.
- Part 2: 14 contact templates (Rahu/Ketu × 7 natal grahas) + cross-rule (Rahu =
  more-of-it; Ketu = release-of-it, same portfolio).
- Part 3: return (18.6y) & half-return (9.3y) semantics.
- Part 4: 6 axis templates, both directions, per-domain leans; favorability flags carried.
- Part 5 showcase (all math python-verified): Rahu enters Makaram 2026-12-07; exact
  contacts **Moon ≈2027-01-09 · Venus ≈2027-04-29 · Saturn ≈2027-06-25 · Mars ≈2027-08-14**;
  exit ≈2028-06-25; factor-D spine Avittam (janma star) →2027-04-11 / Thiruvonam
  →2027-12-19 / Uthiradam →2028-06-25; no node-star intensification; no return/half-return
  in window; both frames fire (4/10 Lagna + 1/7 Moon).
- 3 school notes → GK-10.

### 2026-10-31 10:33 IST — GK-01 delegated to Panduranga; this CHANGELOG established
- **Machan's call**: the factor-D "~40–41 days per nakshatra" discrepancy (GK-01) will be
  **handled by Panduranga** (developer). Gate-kept in this registry — status OPEN ·
  BLOCKING — factor-D sub-period renderer must not be built until Panduranga's resolution
  lands; on resolution, update: this registry, `foundations/rahu-ketu.md` Part 1.1 flag,
  AGENTS.md factor-D line, and `MEMORY.md`.
- **This file created** as the project's consolidated, end-to-end change record; GK
  registry consolidated from all file footers + MEMORY.md ⛔ items (GK-01 … GK-11).

### 2026-10-31 11:08 IST — Milestone 1: report-generation checking order approved + RKT/ORB-02 rules integrated
- **M1 checking order approved "good for now" by Machan** (7 steps): 1 axis placement
  (Moon PRIMARY, lagna where cusps apply) → 2 landlord/dispositor condition → 3 dated
  contact events (+ return/half-return check) → 4 star-by-star sub-period walk →
  5 running dasha-bhukti check → 6 question gate (transit × dasha on the question's
  bhavas → Favorable/Mixed/Challenging) → 7 assemble report.
- **Machan's 4 presentation rulings**: combined reading (Moon primary; lagna only where
  cusps are arrived) · show ALL contacts, highlight by domain relevance (presentation
  freedom granted) · **degree-based asymmetric intensity** (influence starts 3° before
  the natal planet, peaks at exact crossing, declines from the moment of crossing,
  fully gone 2.5° past — drives readings AND timeline language) · tone per REPORT-01.
- **RKT-01..05 adopted and carded into `rule-engine/RULES.md`** (Machan's transit
  framework dump, formalized): RKT-01 umbrella contact rule (natural karakatva +
  functional lordship, two channels) · RKT-02 contacted-planet dasha amplification —
  v1 = MD×bhukti only, Antara/Sookshma → v2 · RKT-03 unoccupied-house transit = mild,
  house-level only · RKT-04 incoming benefic aspects on transit Rahu modify positively
  (conditioned by aspector strength + functional nature; no conflict with node-aspects-
  OFF, which governs outgoing) · RKT-05 Ketu reduction principle + malefic-suppression
  clause (Ketu on natural malefics reduces their harm). Sample-chart check: no natal
  benefic aspects Makaram → RKT-04 dormant in the Dec-2026 showcase.
- **ORB-02 carded** (asymmetric contact curve): window start = natal + 3°, end =
  natal − 2.5°; at 0.05295°/day ≈ 57d rise / 47d fade / ~104d total. Supersedes the
  symmetric ≤3°/≤5° orbs everywhere (AGENTS.md factor-B line, rahu-ketu.md Part 1.3 +
  Part 5 + status footer all updated). New showcase windows: Moon ≈2026-11-14 →
  2027-02-26 · Venus 2027-03-04 → 06-15 · Saturn 2027-04-30 → 08-11 · Mars 2027-06-19 →
  10-01 — the four windows now nearly abut → "one continuous ~11-month contact season
  with four dated peaks" replaces the heavy-overlap reading.
- **NEW FILE: `rule-engine/REPORT-FLOW.md`** — the Milestone-1 deliverable: 7 steps +
  4 rulings in plain language, sample-chart thread through every step, done-checklist
  (awaits Machan's read-through → Milestone 1 LOCKED).
- ⛔ **GK-12 logged** (ORB-02 sign-border question, surfaced by the asymmetric math).
- Next: Machan reads REPORT-FLOW.md → Milestone 1 lock → Milestone 2 (report template,
  gated on GK-08 language).

### 2026-10-31 — Machan's Report Generation Framework → Milestone 2 template skeleton
- **Framework received and formalized** (Machan's dump: background data collection →
  initial natal-profile & transit-overview report → question-specific report).
  Verdict: **no conflicts** — the framework splits the report into Half 1 (who the
  native is + current context) and Half 2 (the transit answer); Half 2 = the approved
  M1 7-step flow, unchanged.
- **Three data sources mapped**: natal data (DOB/time/place → positions from the
  existing software) · panchangam data (already in the software) · question→bhava
  mapping (`kelvigal.md`).
- **NEW RULE CARDS in `rule-engine/RULES.md` — NATAL PROFILE LAYER**: PROF-01 lagna
  analysis · PROF-02 lagna nakshatra analysis · PROF-03 lagna lord placement = life
  gravitation. Sample-chart threads: Thulam lagna → balance/partnership; lagna star
  **Swati p3, lord Rahu** (the report's protagonist rules her rising star — transits
  land personally); lagna lord **Venus in the 4th** (stellium) → life gravitates to
  home/property/foundation — pre-frames the transit landing on that same 4th.
- **NEW FILE: `rule-engine/REPORT-TEMPLATE.md`** — Milestone-2 skeleton: Section 0
  header (DOB/time/place) · Section 1 natal + gocharam charts SIDE-BY-SIDE + running
  dasha-bhukti strip · Section 2 "who you are" (PROF-01..03) · Section 3 "the transit
  now" (M1 steps 1–5) · Section 4 "your question" (M1 steps 6–7) · REPORT-01 tone
  throughout. Determinism lock restated: KB + rules only, byte-identical outputs.
- **GK interactions flagged for Machan's confirm** (registry entries stay OPEN until
  he rules): framework answers **GK-09 #3** (input contract = birth data → positions
  from our software) · framework's domain wording ("any other life matter") suggests
  **GK-07** list is open-ended with kelvigal.md as the card registry · **GK-08**
  (language) now the sole gate for prose emission files.

---

## Next scheduled work (as of 2026-10-31, post-framework)
1. **Machan reads `rule-engine/REPORT-FLOW.md` (M1) + `rule-engine/REPORT-TEMPLATE.md`
   (M2)** → approve/correct → both milestones LOCKED.
2. Machan's confirms: GK-07 (domain list open-ended?) · GK-08 (language) ·
   GK-09 #3 (input contract).
3. **Contact-rules module** (factor B engine) — BLOCKED on Machan's corrections to
   rahu-ketu.md (GK-11) and on GK-01 for its factor-D spine; ORB-02 edge rendering also
   waits on GK-12.
4. Machan's rulings: GK-02 … GK-10, GK-12 queues.
5. Panduranga: GK-01 (and GK-03 implementation leg once Machan confirms the print convention).

### 2026-10-31 — Generative libraries doctrine + pilot decisions
- **Machan's runtime doctrine locked**: two library tiers — foundations (encyclopedic
  facts) + **generative (print-ready report prose)**. Runtime = pure rule matching
  (if/else/loop) → branch's pre-written text → coherent stitching. No AI at runtime.
- **Pilot domain = CAREER** (its lens is already seeded in RULES.md).
- **Drafting language = English first**, translate after approval — partial progress on
  GK-08 (final print language decision remains OPEN).
- Fragment granularity question escalated by Machan ("the deeper, proper way") →
  3-tier architecture proposed, awaiting his ruling.


### 2026-10-31 — Phase 4 engine built end-to-end (Phase 3 banks seeded)
- **Engine v0.1.0 complete** (`engine/vijay_transit/`, Python 3.9 stdlib-only,
  SecOS-11 banner/docstring style throughout):
  constants · models (strict fail-closed chart validation) · ephemeris (ORB-02
  contact dates, sub-period legs) · vimshottari (MD/bhukti) · factsheet
  (factors A–E + RKT-04 aspects) · lenses · verdict (band + fragment keys +
  pattern A/B/C) · library (Tier 1–3 store, fail-closed on missing key)
  · stitcher (blueprint assembly) · report (Sections 0–4) · render_html
  (self-contained HTML, South-Indian 4×4 charts) · cli.
- **Data files**: sample_chart.json (positions locked from earlier session),
  rahu_makaram_2026.json transit window, functional_nature.json (FUNC-01;
  Thulam verified, others standard pending GK-11), lenses/career.json (2/6/10
  core; 11/3/7 modifiers).
- **Generative banks seeded (DRAFT v0.1 English, awaiting Machan's
  correction)**: phrases.json (Tier 1), profile.json (PROF frames),
  career.json (frames + blueprints A/B/C + ANSWER/REASON/CAUTION/EVENT lines).
  Decision recorded: JSON banks are the machine-consumable single source of
  truth; .md mirrors document structure only.
- **Verdict calibration during build** (weights were never numerically locked):
  axis base softened to −1 when neither node favorable (axis sets tone,
  contacts decide); RKT-02 amplifier counts per contacted core-bhava lord
  (cap 2); added Ketu-10th-from-lagna caution. Reproduces the documented
  answer key: **Favorable / pattern A** with Moon+Mars own-bhukti amplifiers,
  yogakaraka landlord, and the documented cautions (axis tide, Rahu×Moon churn,
  Rahu×Mars haste, Ketu-in-10th detachment).
- **Tests: 15/15 green** (`engine/tests/test_engine.py`): all ORB-02 contact
  dates match the rahu-ketu.md showcase (Moon exact 2027-01-09, Mars
  2027-08-14, exit 2028-06-25…); sub-period legs ±1d; dasha agreement holds at
  both peaks; byte-identical double-run; fail-closed on missing fragment key
  and malformed chart.
  - Bug found & fixed: float floor-division at exact nakshatra boundary
    (280.0 // 13°20′) stalled the sub-period walker — epsilon guard added.
  - ORB-02 sign-border rise now extends before ingress per the literal ruling
    (Moon rise 2026-11-14 ✓), flagged `crosses_sign_border` (⛔ GK-12 open).
  - ⛔ GK-03 remains: bhukti boundaries drift ~2–12 days vs the documented
    table (Moon bhukti end computed 2027-04-09 vs printed 2027-04-11);
    year-length ruling still needed from Machan's software.
- **First machine-generated report**: `validation/sample_career_report.html`
  (band Favorable, pattern A) — PRESENTED TO MACHAN for client-style grading;
  corrections go into the banks, never the engine.

### 2026-10-31 — GK-03 reassigned as Panduranga's debt (Machan's call)
- Machan ruled GK-03 a **debt for Panduranga**: registry row updated — after
  the print convention is confirmed, Panduranga closes the residual
  ~2–12-day drift (constant `DASHA_YEAR_DAYS` flip + any render-rounding
  reconciliation against the "Astro Predictors" dasha print).
- Machan will judge the Mars-vs-Moon headline question by reading the full
  generated report (`validation/sample_career_report.html`).

### 2026-10-31 (later) — Rule-ID glossary rollout (Machan's naming convention locked)
- Machan tabled the **bilingual rule-ID naming table** (RKT/SIGN/BHAVA/GATE/DIGN/FUNC/
  STRENGTH/NBR/PARI/QUAL/ORB/REPORT/PROF/KB) with Tamil meanings; ordered: master
  glossary in RULES.md first, then a glossary at the top of every .md.
- **Master GLOSSARY section added to `rule-engine/RULES.md`** (after the header
  blockquote): full prefix table, how-to-read examples (RKT-01, SIGN-04), and register
  notes — KB is a knowledge-base dependency not a rule prefix; ORB-02 exists without
  ORB-01; GK-xx are blockers not rules; M1/M2 are milestone docs not rule IDs.
- **Subset glossaries inserted into 12 files** (scripted, after each file's title line;
  duplicates guarded): all 9 foundations + REPORT-FLOW.md + REPORT-TEMPLATE.md +
  generative/README.md. Each lists only the prefixes actually used in that file plus a
  pointer to the master; REPORT-FLOW/TEMPLATE also gloss GK-xx and their M1/M2 labels.
- One-line glossary pointers added to AGENTS.md, CLAUDE.md, CHANGELOG.md (this file's
  header), MEMORY.md.
- Convention going forward: new rule IDs must follow **PREFIX-NN** from the master
  table; any new prefix is added to the master first, then to the subset glossaries
  of the files that use it.

### 2026-10-31 (later) — New rule RKT-06: chronological multi-planet transit aggregation (Machan's order)
- Machan identified the missing rule: RKT-01/02 evaluate each contact individually, but
  no card governed **consolidating multiple contacts into one chronological narrative**.
- **RKT-06 added to RULES.md** (after RKT-05): independent per-contact evaluation
  (karakatvam + lordships + occupied house + RKT-02 dasha link) → order by exact-peak
  date (= descending natal degree, retrograde walk) → stitch as one date-wise story;
  **each contact keeps its own significance and timing — no merging/averaging/dropping**.
  Worked example = the sample chart's four-contact Makaram season with computed dates
  (Moon 09-Jan-27 → Venus 29-Apr-27 → Saturn 25-Jun-27 → Mars 14-Aug-27).
- **Overlap clause ⏳ PROPOSED, awaiting Machan's nod**: when two ORB-02 windows
  overlap, higher intensity(t) carries the headline, the other reads as named
  rising/fading undertow; hand-offs anchored at exact peaks. (Showcase trigger: Saturn's
  rise begins the same day Venus peaks — 29-Apr-2027; Mars's rise opens while Saturn
  is still separating.)
- **Scope guard written into the card**: RKT-06 governs the chronological transit
  narrative (REPORT-FLOW step 3); the lens's relevance-ranked lead for the question
  answer (steps 6–7) is a separate selection, not overridden. REPORT-FLOW step 3 now
  cross-references RKT-06.
- **Engine gap identified (decision needed from Machan)**: the generated Section 3
  event list is currently **relevance-ordered for the domain**, not chronological.
  Bringing it under RKT-06 = stitcher ordering change (+ bank keys unaffected).
  Parked alongside the pending Mars-vs-Moon headline ruling — same read-through.
- No glossary change: RKT prefix already in master + relevant subset glossaries.

### 2026-10-31 (later) — New rule RKT-07: sequential contact transition (Machan's ruling; resolves RKT-06 overlap clause)
- Machan ruled how overlapping/adjoining contacts must be narrated: **a continuous
  progression, never two isolated events**. Fading current (previous planet's
  karakatvam + adhipathiyam, concluding register) and approaching current (next
  planet's channels, gathering register) are presented as ONE chronological period;
  both windows and both peak dates preserved verbatim; **no degree-equality or
  shared-exact-date assumption** — adjacency inside one contact season is enough.
- **RKT-07 added to RULES.md** (after RKT-06) with the 5-point requirement list and
  worked sample-chart example: Venus→Saturn hand-off (Venus peaks 29-Apr-27 the same
  day Saturn's rise begins; Venus fades to 16-Jun-27 while Saturn gathers to
  25-Jun-27) and Saturn→Mars (Mars rise 19-Jun-27 during Saturn's separation; Mars
  peak 14-Aug-27, three days after Saturn's release).
- **RKT-06 overlap clause resolved in place**: ⏳ proposal replaced by a pointer to
  RKT-07 (Machan's ruling supersedes the "higher intensity leads" proposal).
- REPORT-FLOW step 3 cross-reference extended to RKT-07.
- **Engine/bank impact (queued, not yet applied)**: transition narration is Tier-3
  blueprint + bank work (fading/rising frame pairs per contact hand-off) plus the
  already-parked RKT-06 chronological-ordering change in the stitcher. Both land
  after Machan's report read-through batch (Mars/Moon ruling + grading).

### 2026-10-31 (later) — Consolidated rule update (Machan's instruction set: RKT-06…09, ORB-02, GATE-02, RKT-04, REPORT-01)
- **New rules**:
  - **GATE-02 — DBAS separation (events vs planetary characteristics)** 🔒: planets
    describe qualities (karakatvam/adhipathiyam); bhavas + DBAS govern event
    manifestation. ORB intensity (how loud) and DBAS connection (whether/when) are
    separate dimensions, never conflated; a low-intensity contact can still carry
    high event relevance when DBAS activates its lordships. RKT-02 v1 scope
    (MD × bhukti) explicitly preserved — no Antara/Sookshma until v2 approval.
  - **RKT-08 — Nakshatra-lord governance of a transit segment** 🔒: no-contact star
    legs are governed by the star lord across TWO channels (natal profile + current
    transit profile). **50% effectiveness reduction** if the lord is debilitated
    natally OR in transit — applied ONCE (both charts ⇒ still 50%); reduced
    qualification, never cancellation; NBR via existing NBR-01/02 only. Machan's
    Uttara-Phalguni/Sun example + sample-chart Shravana(Moon)/Uttarashada(Sun) tail
    legs documented. Clause-B data feed parked as ⛔ GK-13.
  - **RKT-09 — Star-lord activation during inter-contact gaps** 🔒: gaps between
    contact windows are never empty — apply RKT-08 + DBAS check; direct-contact
    influence vs star-lord-mediated influence kept distinct inside one continuous
    narrative. Sample-chart examples: the 6-day Avittam bridge (26-Feb→04-Mar-27,
    Mars-lorded) and the post-Mars tail (01-Oct-27 → 25-Jun-28).
- **Existing rules modified (in place, no duplication)**:
  - **ORB-02**: GK-12 RESOLVED — sign-boundary independence locked; early-influence
    register (mild/probabilistic phrasing); traditional duration guidance (Rahu ~1.5 mo
    / Saturn ~2.5 mo / Jupiter ~1 mo early) recorded as explanatory only — the degree
    curve remains the mechanism. Engine already behaves this way (`crosses_sign_border`
    flag now informational).
  - **RKT-06**: equal/near-degree clause added — exact same degree ⇒ simultaneous
    activation of both planets (both channels, benefic+malefic mix communicated);
    minute-level differences preserve true chronological order; no artificial priority.
  - **RKT-07**: rising/fading intensity communication added — ORB-02 percentages in
    the narrative ("Venus ≈30% fading, Saturn ≈70% rising"), dominant-emerging vs
    diminishing; percentages are curve-computed intensity, never event probability
    (GATE-02 guard).
  - **RKT-04**: integration clause — benefic influence evaluated via strength +
    functional nature, read through karakatvam/adhipathiyam as encouragement toward
    constructive effort; never an automatic positive-event guarantee.
  - **REPORT-01**: strengthened to a global positive-dominant standard (profiles,
    DB readings, transit reports, question predictions); proportionate rule-supported
    cautions only; the four preferred Tamil expressions recorded; absolute constraint —
    never frighten/shame/discourage, never hopeless/helpless, no fabricated positives,
    no suppressed rule-supported cautions.
- **Cross-references updated**: REPORT-FLOW step 3 (GK-12 note → resolved) and step 4
  (RKT-08/09 pointer); RULES.md Pending section refreshed (stale contact-rules line
  replaced; GK-13, Mars/Moon ruling, v2 KP gate listed).
- **Validation (per Machan's §9)**: RKT-06 (order + preserve) × RKT-07 (transition
  register + intensity) × RKT-08/09 (mediated segments) verified non-contradictory —
  direct contact vs star-lord mediation are distinct channels; ORB intensity,
  star-lord quality, DBAS event support and benefic modifiers remain four separate
  evaluation dimensions; all pre-existing locked cards intact; no new astrological
  principles introduced beyond Machan's stated decisions.
- **Awaiting Machan**: GK-13 feed decision; Mars/Moon headline ruling; bank/engine
  implementation order for the RKT-06/07/08/09 rendering gaps.

### 2026-11-01 — Project pushed to personal GitHub
- Repo: `sujansuresh/astro-core`, branch **`astro-engine`** (159 files, commit `8753c6b`).
- Auth: dedicated SSH keypair `~/.ssh/id_ed25519_github_personal` + host alias
  `github.com-personal` (ssh.github.com:443 — port 22 blocked on this network).
  Groww GitHub (gh keyring, HTTPS, sujans_groww) untouched.
- **Deviation**: remote `vijay-transit` branch was found non-empty (unrelated
  "Titus Arith" upload, 10 commits, newest 2026-10-31 23:29). Machan chose
  non-destructive push to a fresh branch `astro-engine`; Titus Arith branches
  (`main`, `vijay-transit`, `sujansuresh-patch-titusarithmatics`) left as-is.

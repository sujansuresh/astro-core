# REPORT-TEMPLATE.md — Milestone 2: The report's page-by-page skeleton

---

## GLOSSARY — Rule ID prefixes used in this file

> Master table: `rule-engine/RULES.md` → GLOSSARY. Only the prefixes used in this file are listed below.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| ORB | Orb / Contact Window | கிரகத் தொடுதலின் டிகிரி மற்றும் கால அளவு |
| REPORT | Report Generation | அறிக்கை உருவாக்கும் விதிகள் |
| PROF | Natal Profile | ஜாதகரின் அடிப்படைப் பண்புகள் |

- **GK-xx** entries cited here (e.g., GK-07/08/09) are project blockers tracked in `CHANGELOG.md`, not rules.
- **M2** is this document's milestone label, not a rule ID.

---

> **Status**: DRAFT from Machan's Report Generation Framework (2026-10-31), awaiting his
> read-through and corrections. This document fixes the **shape of the report** — what
> appears, in what order. The transit-question engine that fills Half 2 is the approved
> 7-step flow (`REPORT-FLOW.md`); the profile rule cards are PROF-01..03 in `RULES.md`.
> Language of the emitted prose is gated on GK-08 (Tamil / English / both) — this
> skeleton is language-neutral.
>
> **Determinism lock**: every word rendered comes from the precomputed knowledge
> libraries and the rule engine — no runtime AI. Same inputs → byte-identical report.

---

## The three background data sources (Machan's framework, section 1)

| # | Source | What it provides | Where it lives in this project |
|---|---|---|---|
| 1 | **Natal chart data** | Birth details, planetary positions, ascendant, houses, significations | User's DOB / time / place → computed by our existing astrology software (input contract — pending GK-09 confirm) |
| 2 | **Panchangam data** | Astronomical / panchangam information, transit (gocharam) positions | Already in our software; transit windows per `foundations/rahu-ketu.md` |
| 3 | **Question-specific house mapping** | The bhavas and significations tied to the user's question | `foundations/kelvigal.md` (50 question cards) |

The user's question may concern any domain — career, marriage, finance, property,
health, education, business, foreign opportunities, or any other life matter
(domain list reads open-ended — pending GK-07 confirm).

---

## The report, page by page

### Section 0 — Header block
- Date of birth · time of birth · place of birth (as given by the user).

### Section 1 — The two charts, side by side
- **Natal horoscope chart** and **current transit (gocharam) chart**, displayed
  side-by-side for easy comparison.
- A single line beneath: **currently running Dasha–Bhukti** (with its end date).

*Sample chart*: Thulam lagna natal chart beside the gocharam chart showing Rahu in
Makaram / Ketu in Katakam; strip reads "Jupiter Maha Dasha — Moon Bhukti (till
11-Apr-2027)".

### Section 2 — Who you are (the natal profile)
Three short layers, one paragraph each (rule cards PROF-01..03):
1. **Your lagna** — the ascendant's character (PROF-01).
2. **Your lagna star** — the nakshatra on the ascendant degree and its lord (PROF-02).
3. **Where your life gravitates** — the lagna lord's house and what it pulls you
   toward (PROF-03).

*Sample chart*: "Thulam rising — balance-seeking, partnership-oriented… Your rising
star is Swati, ruled by Rahu — independence and self-made movement… Your lagna lord
Venus sits in your 4th house — home, property and foundation draw your life's
attention…"

### Section 3 — The transit now (context before the question)
The question-independent transit picture — steps 1–5 of the M1 flow
(`REPORT-FLOW.md`): axis placement (Moon primary, lagna where cusps apply) → landlord
condition → the dated contact calendar (rise–peak–release per ORB-02) → star-by-star
sub-period flow → running period agreement.

### Section 4 — Your question (the answer)
Steps 6–7 of the M1 flow: the question's houses are read against transit × period →
the verdict band (Favorable / Mixed / Challenging) with named reasons → the dated
timeline of the window, with the domain-relevant contacts highlighted and all other
contacts still shown (Machan's show-all ruling).

### Closing tone (all sections)
REPORT-01 throughout: positives lead (~80%); risks are stated as soft possibilities
with a caution note, never as fixed doom.

---

## The generation philosophy (Machan, restated as the build order)

1. Establish who the individual is, astrologically (Sections 0–2).
2. Establish the current planetary and transit context (Section 3).
3. Understand the question; identify its houses (kelvigal mapping).
4. Apply the corresponding rule sets (M1 flow).
5. Deliver the personalised, question-specific interpretation and prediction.

## Done-checklist for Milestone 2
- [x] Template shape fixed (this document)
- [x] Profile rule cards (PROF-01..03 in RULES.md)
- [ ] Machan's read-through + corrections → **Milestone 2 LOCKED**
- [ ] GK-08 language decision → prose emission files
- [ ] GK-07 domain list confirm (open-ended vs fixed set)
- [ ] GK-09 input-contract confirm (DOB/time/place → positions from our software)

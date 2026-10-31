"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/constants.py                                 ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Single source of truth for every locked astrological constant    ║
║  LAYER:    Foundation / Configuration                                        ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Hold ONLY values that are locked in AGENTS.md / rule-engine/RULES.md.   ║
║  2. Carry the provenance of each value (which card / which GK item).        ║
║  3. Fail the build loudly if a pending ruling (GK-xx) would change a value  ║
║     — pending values are marked with their GK ID in-line.                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - No computation happens here; this module is data-only.                   ║
║  - No value may be edited without a corresponding CHANGELOG entry.          ║
║  - Sign and nakshatra names use the project's Tamil conventions exactly as  ║
║    they appear in foundations/ (Makaram, Avittam, …).                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Zodiac frame (locked: sidereal, whole-sign houses — AGENTS.md conventions)
# ---------------------------------------------------------------------------

#: The twelve signs in zodiac order, project Tamil naming.
SIGNS = [
    "Mesham", "Rishabam", "Mithunam", "Katakam", "Simmam", "Kanni",
    "Thulam", "Vrischikam", "Dhanus", "Makaram", "Kumbam", "Meenam",
]

#: Lord of each sign, same order as SIGNS (Parashari standard).
SIGN_LORDS = [
    "Mars", "Venus", "Mercury", "Moon", "Sun", "Mercury",
    "Venus", "Mars", "Jupiter", "Saturn", "Saturn", "Jupiter",
]

# ---------------------------------------------------------------------------
# Nakshatras (27 × 13°20' each; lord sequence = Vimshottari order)
# ---------------------------------------------------------------------------

#: Nakshatra names in zodiac order, project Tamil naming (foundations/nakshatras.md).
NAKSHATRAS = [
    "Ashwini", "Bharani", "Karthigai", "Rohini", "Mirugasiridam",
    "Thiruvathirai", "Punarpoosam", "Poosam", "Ayilyam", "Magham",
    "Pooram", "Uthiram", "Hastham", "Chithirai", "Swathi",
    "Visakam", "Anusham", "Kettai", "Moolam", "Pooradam",
    "Uthiradam", "Thiruvonam", "Avittam", "Sadayam", "Poorattathi",
    "Uthirattathi", "Revathi",
]

#: Vimshottari lord sequence, index-aligned by nakshatra_index % 9.
DASHA_SEQUENCE = [
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
]

#: Vimshottari Maha Dasha year lengths (total 120).
DASHA_YEARS = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
    "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17,
}

NAKSHATRA_SPAN_DEG = 13.0 + 20.0 / 60.0  # 13°20'
PADA_SPAN_DEG = NAKSHATRA_SPAN_DEG / 4.0

# ---------------------------------------------------------------------------
# Mean-node motion (locked: report MEAN node — AGENTS.md; rahu-ketu.md Part 1)
# ---------------------------------------------------------------------------

#: Mean node retrograde speed in degrees/day (360° / 6,798 d sidereal cycle).
#: Provenance: foundations/rahu-ketu.md Part 1.1 (python-verified against the
#: Dec-2026 showcase dates). Byte-parity with "Astro Predictors" pending GK-02/03.
MEAN_NODE_SPEED_DEG_PER_DAY = 0.05295

# ---------------------------------------------------------------------------
# ORB-02 — degree-based asymmetric contact curve (Machan, 2026-10-31, locked)
# ---------------------------------------------------------------------------

#: Influence begins when the node is this many degrees BEFORE the natal planet
#: (the node walks retrograde, so it approaches from the higher degree).
ORB_APPLY_DEG = 3.0

#: Influence is fully gone once the node is this many degrees PAST the planet.
ORB_SEPARATE_DEG = 2.5

#: Sign-border behaviour for the applying edge is PENDING GK-12 — the engine
#: currently lets the rise begin before ingress (Machan's literal ruling) and
#: flags every such contact with ``crosses_sign_border=True``.
# ---------------------------------------------------------------------------
# Axis favorability (locked: AGENTS.md factor A)
# ---------------------------------------------------------------------------

RAHU_FAVORABLE_HOUSES = frozenset({3, 6, 10, 11})
KETU_FAVORABLE_HOUSES = frozenset({3, 6, 11})

# ---------------------------------------------------------------------------
# Natural benefics / malefics (RKT-04 / RKT-05 conditioning)
# ---------------------------------------------------------------------------

NATURAL_BENEFICS = frozenset({"Jupiter", "Venus", "Mercury"})  # + waxing Moon (computed)
NATURAL_MALEFICS = frozenset({"Sun", "Mars", "Saturn"})        # + waning Moon (computed)

# ---------------------------------------------------------------------------
# Dignity tables (factor C — own sign / exaltation / debilitation)
# ---------------------------------------------------------------------------

EXALTATION_SIGN = {
    "Sun": "Mesham", "Moon": "Rishabam", "Mars": "Makaram",
    "Mercury": "Kanni", "Jupiter": "Katakam", "Venus": "Meenam",
    "Saturn": "Thulam",
}
DEBILITATION_SIGN = {
    "Sun": "Thulam", "Moon": "Vrischikam", "Mars": "Katakam",
    "Mercury": "Meenam", "Jupiter": "Makaram", "Venus": "Kanni",
    "Saturn": "Mesham",
}
OWN_SIGNS = {
    "Sun": ["Simmam"], "Moon": ["Katakam"], "Mars": ["Mesham", "Vrischikam"],
    "Mercury": ["Mithunam", "Kanni"], "Jupiter": ["Dhanus", "Meenam"],
    "Venus": ["Rishabam", "Thulam"], "Saturn": ["Makaram", "Kumbam"],
}

# ---------------------------------------------------------------------------
# Vimshottari year length — ⛔ GK-03 PENDING (360d classical vs 365.25d civil)
# ---------------------------------------------------------------------------

#: Days per dasha year. Default civil 365.25 until Machan confirms what
#: "Astro Predictors" prints (GK-03); flip this one constant on his ruling.
DASHA_YEAR_DAYS = 365.25

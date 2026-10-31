"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/factsheet.py                                 ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Assemble the complete FACT SHEET the rule engine reasons over    ║
║  LAYER:    Computation (factors A–E collector)                              ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Factor A — axis favorability (Rahu/Ketu houses from Moon, RKT-01).      ║
║  2. Factor B — contact windows with strength metadata (landlord, dignity,   ║
║     star-lord chain, lordship portfolio of each contacted planet).          ║
║  3. Factor C — dignity of contacted planets (own/exalted/debilitated).      ║
║  4. Factor D — nakshatra sub-period legs of the window.                     ║
║  5. Factor E — Vimshottari MD/bhukti context at every contact peak (RKT-02) ║
║  6. RKT-04 — benefic/malefic aspects ON the transiting nodes (softeners /   ║
║     pressure lines). Node functional nature via dispositor proxy.           ║
║  7. RKT-03 / RKT-05 — the Ketu (empty-sign) mild leg + conditioning notes.  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Output is a plain dict tree — JSON-serialisable, byte-stable for the     ║
║    same inputs (report reproducibility gate).                               ║
║  - Aspect model is whole-sign from the natal planet's position:             ║
║    Jupiter 5/7/9, Mars 4/7/8, Saturn 3/7/10, all others 7th only.           ║
║  - Moon is benefic when waxing: Sun–Moon elongation < 180°.                 ║
║  - No verdict wording lives here — this layer emits FACTS ONLY.             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional

from .constants import (
    DEBILITATION_SIGN, EXALTATION_SIGN, KETU_FAVORABLE_HOUSES,
    NATURAL_BENEFICS, NATURAL_MALEFICS, OWN_SIGNS, RAHU_FAVORABLE_HOUSES,
    SIGNS,
)
from .ephemeris import ContactWindow, SubPeriod, TransitCalculator
from .models import NatalChart, TransitWindow
from .vimshottari import DashaPeriod, compute_maha_dashas, period_on

#: Special whole-sign aspects per planet (the 7th applies to every planet).
SPECIAL_ASPECTS = {
    "Jupiter": (5, 7, 9),
    "Mars": (4, 7, 8),
    "Saturn": (3, 7, 10),
}
DEFAULT_ASPECTS = (7,)

#: Houses whose occupation gives a planet directional strength (digbala).
DIGBALA_HOUSE = {"Jupiter": 1, "Mercury": 1, "Moon": 4, "Venus": 4,
                 "Saturn": 7, "Sun": 10, "Mars": 10}


def _dignity(planet: str, sign: str) -> str:
    """Own / exalted / debilitated / neutral dignity of a planet in a sign."""
    if sign in OWN_SIGNS.get(planet, []):
        return "own"
    if EXALTATION_SIGN.get(planet) == sign:
        return "exalted"
    if DEBILITATION_SIGN.get(planet) == sign:
        return "debilitated"
    return "neutral"


class FactSheetBuilder:
    """
    Builds the full fact sheet for one (natal chart × transit window) pair.

    Business Intent:
        Every downstream layer (lens, verdict, stitcher) reads ONLY this sheet.
        Keeping fact collection in one pass guarantees the verdict and the
        printed report can never disagree about what the chart contains.
    """

    def __init__(self, chart: NatalChart, transit: TransitWindow,
                 functional_nature: Dict[str, Dict[str, str]]):
        self._chart = chart
        self._transit = transit
        self._nature = functional_nature[chart.lagna_sign]
        self._calc = TransitCalculator(transit)

    def build(self) -> dict:
        """
        Compute the complete fact sheet.

        Returns:
            dict tree: axis, landlord, contacts[], sub_periods[], dasha context,
            aspects on nodes, conditioning notes. All dates ISO strings.
        """
        contacts = self._calc.contact_windows(self._chart)
        timeline = compute_maha_dashas(
            self._chart.planets["Moon"].absolute_longitude,
            date.fromisoformat(self._chart.native["birth_date"]))
        return {
            "axis": self._axis(),
            "landlord": self._landlord(),
            "contacts": [self._contact_fact(c, timeline) for c in contacts],
            "sub_periods": [self._sub_period_fact(s) for s in
                            self._calc.sub_periods()],
            "aspects_on_nodes": self._aspects_on_nodes(),
            "dasha_now": self._dasha_at(timeline, self._calc.ingress),
            "window": {
                "rahu_sign": self._transit.sign,
                "ketu_sign": SIGNS[(SIGNS.index(self._transit.sign) + 6) % 12],
                "ingress": self._transit.ingress_iso,
                "exit": self._calc.exit_date().isoformat(),
            },
        }

    # -- factor A ------------------------------------------------------------
    def _axis(self) -> dict:
        """Rahu/Ketu houses from the Moon (primary) and their favorability."""
        rahu_house = self._chart.house_from_moon(self._transit.sign)
        ketu_house = (rahu_house + 6 - 1) % 12 + 1
        return {
            "rahu_house_from_moon": rahu_house,
            "ketu_house_from_moon": ketu_house,
            "rahu_house_from_lagna":
                self._chart.house_from_lagna(self._transit.sign),
            "ketu_house_from_lagna": (self._chart.house_from_lagna(
                self._transit.sign) + 6 - 1) % 12 + 1,
            "rahu_favorable": rahu_house in RAHU_FAVORABLE_HOUSES,
            "ketu_favorable": ketu_house in KETU_FAVORABLE_HOUSES,
        }

    # -- landlord (dispositor of the transit sign) ----------------------------
    def _landlord(self) -> dict:
        """Nature + condition of the transit-sign lord (the 'landlord')."""
        rahu_sign_lord = self._chart.lord_of_house(
            self._chart.house_from_lagna(self._transit.sign))
        p = self._chart.planets[rahu_sign_lord]
        return {
            "planet": rahu_sign_lord,
            "sign": p.sign,
            "house_from_lagna": self._chart.house_from_lagna(p.sign),
            "dignity": _dignity(rahu_sign_lord, p.sign),
            "functional_nature": self._nature[rahu_sign_lord],
            "is_yogakaraka": self._nature[rahu_sign_lord] == "yogakaraka",
            "digbala": self._chart.house_from_lagna(p.sign) ==
                       DIGBALA_HOUSE.get(rahu_sign_lord, -1),
        }

    # -- factor B/C contacts --------------------------------------------------
    def _contact_fact(self, c: ContactWindow,
                      timeline: List[DashaPeriod]) -> dict:
        """Full fact record for one node × natal-planet contact."""
        planet = c.planet
        house_lagna = self._chart.house_from_lagna(planet.sign)
        star_lord = planet.nakshatra_lord
        md, bhukti = period_on(timeline, c.exact_peak) or (None, None)
        return {
            "node": c.node,
            "planet": planet.name,
            "planet_sign": planet.sign,
            "planet_degree": round(planet.degree, 2),
            "house_from_lagna": house_lagna,
            "houses_owned": self._chart.houses_owned_by(planet.name),
            "functional_nature": self._nature.get(planet.name, "neutral"),
            "dignity": _dignity(planet.name, planet.sign),
            "retrograde": planet.retrograde,
            "digbala": house_lagna == DIGBALA_HOUSE.get(planet.name, -1),
            "nakshatra": planet.nakshatra,
            "nakshatra_pada": planet.pada,
            "star_lord": star_lord,
            "star_lord_nature": self._nature.get(star_lord, "neutral"),
            "star_lord_houses": self._chart.houses_owned_by(star_lord),
            "rise_begins": c.rise_begins.isoformat(),
            "exact_peak": c.exact_peak.isoformat(),
            "fully_released": c.fully_released.isoformat(),
            "crosses_sign_border": c.crosses_sign_border,
            "dasha_at_peak": {
                "maha_dasha": md.lord if md else None,
                "bhukti": bhukti.lord if bhukti else None,
                "bhukti_is_planet": bool(bhukti and
                                         bhukti.lord == planet.name),
                "bhukti_is_star_lord": bool(bhukti and
                                            bhukti.lord == star_lord),
            },
        }

    # -- factor D -------------------------------------------------------------
    def _sub_period_fact(self, s: SubPeriod) -> dict:
        return {"nakshatra": s.nakshatra, "lord": s.lord,
                "lord_nature": self._nature.get(s.lord, "neutral"),
                "begins": s.begins.isoformat(), "ends": s.ends.isoformat()}

    # -- RKT-04 aspects on the transiting nodes -------------------------------
    def _aspects_on_nodes(self) -> dict:
        """
        Which natal planets aspect the Rahu / Ketu transit signs, and whether
        each is a benefic (softens) or malefic (adds pressure) for this lagna
        + by nature. Moon benefic when waxing (elongation Sun→Moon < 180°).
        """
        moon_lon = self._chart.planets["Moon"].absolute_longitude
        sun_lon = self._chart.planets["Sun"].absolute_longitude
        waxing = (moon_lon - sun_lon) % 360.0 < 180.0

        def natural(name: str) -> str:
            if name == "Moon":
                return "benefic" if waxing else "malefic"
            if name in NATURAL_BENEFICS:
                return "benefic"
            return "malefic"

        result = {"Rahu": [], "Ketu": []}
        ketu_sign = SIGNS[(SIGNS.index(self._transit.sign) + 6) % 12]
        for planet in self._chart.planets.values():
            if planet.name in ("Rahu", "Ketu"):
                continue  # nodes do not cast classical aspects here
            from_idx = SIGNS.index(planet.sign)
            for offset in SPECIAL_ASPECTS.get(planet.name, DEFAULT_ASPECTS):
                aspected = SIGNS[(from_idx + offset - 1) % 12]
                for node, sign in (("Rahu", self._transit.sign),
                                   ("Ketu", ketu_sign)):
                    if aspected == sign:
                        result[node].append({
                            "planet": planet.name,
                            "aspect_ordinal": offset,
                            "natural": natural(planet.name),
                            "functional_nature":
                                self._nature.get(planet.name, "neutral"),
                        })
        return result

    # -- factor E -------------------------------------------------------------
    @staticmethod
    def _dasha_at(timeline: List[DashaPeriod], when: date) -> dict:
        md, bhukti = period_on(timeline, when) or (None, None)
        return {
            "maha_dasha": md.lord if md else None,
            "maha_dasha_ends": md.ends.isoformat() if md else None,
            "bhukti": bhukti.lord if bhukti else None,
            "bhukti_ends": bhukti.ends.isoformat() if bhukti else None,
        }


def load_functional_nature(path: Path) -> Dict[str, Dict[str, str]]:
    """
    Load the FUNC-01 12-lagna functional-nature matrix.

    Raises / Fallbacks:
        ChartInputError-style ValueError if a lagna or planet entry is absent —
        the engine refuses to judge with a partial matrix.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    required_planets = {"Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus",
                        "Saturn"}
    for sign, table in data.items():
        if sign.startswith("_"):  # provenance / metadata keys
            continue
        if sign not in SIGNS:
            raise ValueError(f"functional_nature: unknown lagna key {sign}")
        missing = required_planets - set(table)
        if missing:
            raise ValueError(
                f"functional_nature[{sign}] missing: {sorted(missing)}")
    return data

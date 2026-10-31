"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/models.py                                    ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Typed, validated data structures for natal charts & transits     ║
║  LAYER:    Domain model                                                      ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Parse and STRICTLY validate the natal-chart JSON handed over by the     ║
║     astrology software (positions are computed upstream — GK-09 leg).       ║
║  2. Expose derived lookups used everywhere: absolute longitude, whole-sign  ║
║     house from lagna / from Moon, nakshatra + pada, house lords.            ║
║  3. Represent the transit (gocharam) window definition.                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - All validation fails CLOSED: a malformed chart raises ChartInputError    ║
║    with the offending field named; the engine never guesses a position.     ║
║  - Houses are whole-sign from the reference point (AGENTS.md conventions).  ║
║  - Nodes in the natal chart must satisfy Ketu = Rahu + 180° (checked).      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from .constants import (
    DASHA_SEQUENCE, NAKSHATRAS, NAKSHATRA_SPAN_DEG, PADA_SPAN_DEG,
    SIGN_LORDS, SIGNS,
)

PLANET_NAMES = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn",
                "Rahu", "Ketu"]


class ChartInputError(ValueError):
    """The natal/transit JSON failed validation; the named field must be fixed."""


@dataclass(frozen=True)
class Planet:
    """One natal graha: sign + degree within sign + retrograde flag."""
    name: str
    sign: str
    degree: float
    retrograde: bool = False

    @property
    def absolute_longitude(self) -> float:
        """Sidereal longitude 0–360 (whole-sign frame)."""
        return SIGNS.index(self.sign) * 30.0 + self.degree

    @property
    def nakshatra_index(self) -> int:
        return int(self.absolute_longitude // NAKSHATRA_SPAN_DEG)

    @property
    def nakshatra(self) -> str:
        return NAKSHATRAS[self.nakshatra_index]

    @property
    def pada(self) -> int:
        within = self.absolute_longitude % NAKSHATRA_SPAN_DEG
        return int(within // PADA_SPAN_DEG) + 1

    @property
    def nakshatra_lord(self) -> str:
        return DASHA_SEQUENCE[self.nakshatra_index % 9]


@dataclass(frozen=True)
class NatalChart:
    """Validated natal chart: native metadata + lagna + nine grahas."""
    native: Dict[str, str]
    lagna_sign: str
    lagna_degree: float
    planets: Dict[str, Planet]

    # -- derived lookups ----------------------------------------------------
    @property
    def lagna(self) -> Planet:
        return Planet("Lagna", self.lagna_sign, self.lagna_degree)

    @property
    def moon_sign(self) -> str:
        return self.planets["Moon"].sign

    def house_from_lagna(self, sign: str) -> int:
        """Whole-sign house of ``sign`` counted from the lagna sign."""
        return (SIGNS.index(sign) - SIGNS.index(self.lagna_sign)) % 12 + 1

    def house_from_moon(self, sign: str) -> int:
        """Whole-sign house of ``sign`` counted from the Moon sign (PRIMARY frame)."""
        return (SIGNS.index(sign) - SIGNS.index(self.moon_sign)) % 12 + 1

    def lord_of_house(self, house: int) -> str:
        """Lord of the lagna-relative house number (1–12)."""
        sign = SIGNS[(SIGNS.index(self.lagna_sign) + house - 1) % 12]
        return SIGN_LORDS[SIGNS.index(sign)]

    def houses_owned_by(self, planet: str) -> List[int]:
        """Lagna-relative houses whose signs this planet lords."""
        return [h for h in range(1, 13) if self.lord_of_house(h) == planet]

    def occupants_of_house(self, house: int) -> List[Planet]:
        """Natal grahas sitting in the given lagna-relative house."""
        return [p for p in self.planets.values()
                if self.house_from_lagna(p.sign) == house]

    # -- loading ------------------------------------------------------------
    @classmethod
    def from_json(cls, path: Path) -> "NatalChart":
        """
        Load and validate a natal-chart JSON file produced by the astro software.

        Raises / Fallbacks:
            ChartInputError: any missing field, unknown sign, out-of-range
            degree, unknown planet key, or broken Rahu/Ketu opposition. The
            engine refuses to proceed on a chart it cannot trust.
        """
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        for field in ("native", "lagna", "planets"):
            if field not in raw:
                raise ChartInputError(f"missing top-level field: {field}")
        lagna = raw["lagna"]
        if lagna.get("sign") not in SIGNS:
            raise ChartInputError(f"lagna.sign unknown: {lagna.get('sign')}")
        planets: Dict[str, Planet] = {}
        for name, pdata in raw["planets"].items():
            if name not in PLANET_NAMES:
                raise ChartInputError(f"unknown planet key: {name}")
            sign, degree = pdata.get("sign"), pdata.get("degree")
            if sign not in SIGNS:
                raise ChartInputError(f"{name}.sign unknown: {sign}")
            if not isinstance(degree, (int, float)) or not 0.0 <= degree < 30.0:
                raise ChartInputError(f"{name}.degree out of range [0,30): {degree}")
            planets[name] = Planet(name, sign, float(degree),
                                   bool(pdata.get("retrograde", False)))
        missing = set(PLANET_NAMES) - set(planets)
        if missing:
            raise ChartInputError(f"missing planets: {sorted(missing)}")
        rahu, ketu = planets["Rahu"], planets["Ketu"]
        delta = abs((rahu.absolute_longitude - ketu.absolute_longitude) % 360.0)
        if abs(delta - 180.0) > 0.01:
            raise ChartInputError("Rahu/Ketu are not exactly opposite")
        return cls(native=raw["native"], lagna_sign=lagna["sign"],
                   lagna_degree=float(lagna["degree"]), planets=planets)


@dataclass(frozen=True)
class TransitWindow:
    """
    One nodal sign-transit (gocharam) window as published by the panchangam.

    The ingress date and mean speed come from the software's panchangam data
    (framework source #2); the engine never re-derives ingress from astronomy,
    keeping byte-parity with the printed ephemeris (GK-02/GK-03 note).
    """
    node: str          # "Rahu" (Ketu is always the opposite sign)
    sign: str
    ingress_iso: str   # YYYY-MM-DD
    speed_deg_per_day: float

    @classmethod
    def from_json(cls, path: Path) -> "TransitWindow":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
        if raw.get("node") != "Rahu":
            raise ChartInputError("transit definition must be anchored on Rahu")
        if raw.get("sign") not in SIGNS:
            raise ChartInputError(f"transit.sign unknown: {raw.get('sign')}")
        speed = float(raw.get("speed_deg_per_day", 0))
        if speed <= 0:
            raise ChartInputError("transit.speed_deg_per_day must be positive")
        return cls(node="Rahu", sign=raw["sign"],
                   ingress_iso=str(raw["ingress"]), speed_deg_per_day=speed)

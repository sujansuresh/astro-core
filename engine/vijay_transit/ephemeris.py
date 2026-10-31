"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/ephemeris.py                                 ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Contact-date arithmetic (factor B mechanics + ORB-02 curve)      ║
║  LAYER:    Computation                                                       ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Compute every natal-planet contact of the transiting node pair inside   ║
║     the window — rise / exact-peak / full-release dates per ORB-02.         ║
║  2. Emit contacts in retrograde order (highest natal degree first).         ║
║  3. Compute the nakshatra sub-period legs (factor D spine) of the window.   ║
║  4. Expose the node's degree on any date (for timeline rendering).          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Pure arithmetic: ingress date + constant mean speed. No ephemeris lib.   ║
║  - Mean node ⇒ every contact is ONE contiguous window (rahu-ketu.md 1.2).   ║
║  - ORB-02 asymmetric curve: start = natal+3° (applying), end = natal−2.5°   ║
║    (separating). A rise may cross the sign border — flagged, not clamped    ║
║    (behaviour pending GK-12; Machan's literal ruling governs today).        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import List

from .constants import (
    MEAN_NODE_SPEED_DEG_PER_DAY, NAKSHATRA_SPAN_DEG, NAKSHATRAS,
    DASHA_SEQUENCE, ORB_APPLY_DEG, ORB_SEPARATE_DEG, SIGNS,
)
from .models import NatalChart, Planet, TransitWindow

SIGN_SPAN_DEG = 30.0


@dataclass(frozen=True)
class ContactWindow:
    """One node × natal-planet contact with its ORB-02 rise/peak/release dates."""
    node: str
    planet: Planet
    rise_begins: date
    exact_peak: date
    fully_released: date
    crosses_sign_border: bool  # rise begins before the node's ingress (GK-12 flag)


@dataclass(frozen=True)
class SubPeriod:
    """One nakshatra leg of the sign transit (factor D spine)."""
    nakshatra: str
    lord: str
    begins: date
    ends: date


class TransitCalculator:
    """
    All date arithmetic for one nodal transit window.

    Business Intent:
        Centralizes every date the report prints so the whole product shares one
        motion model; if the panchangam parity ruling (GK-02/GK-03) changes the
        ingress or speed, exactly one input file changes and every downstream
        date moves together.
    """

    def __init__(self, transit: TransitWindow):
        self._t = transit
        self._ingress = date.fromisoformat(transit.ingress_iso)

    @property
    def ingress(self) -> date:
        return self._ingress

    def _date_at_degree(self, degree_in_sign: float) -> date:
        """Date the retrograde node reaches ``degree_in_sign`` (ingress = 30°)."""
        travelled = SIGN_SPAN_DEG - degree_in_sign
        return self._ingress + timedelta(
            days=travelled / self._t.speed_deg_per_day)

    def exit_date(self) -> date:
        """Date Rahu leaves the sign (reaches 0°00')."""
        return self._date_at_degree(0.0)

    def contact_windows(self, chart: NatalChart) -> List[ContactWindow]:
        """
        Every natal planet conjoined by Rahu (in transit sign) or Ketu (opposite
        sign), in retrograde contact order, with ORB-02 windows.

        Args:
            chart: validated natal chart.

        Returns:
            List[ContactWindow], highest natal degree first (Part 1.4 ordering).
            Contacts are conjunction-only — node aspects are OFF by lock.
        """
        ketu_sign = SIGNS[(SIGNS.index(self._t.sign) + 6) % 12]
        windows: List[ContactWindow] = []
        for node, sign in (("Rahu", self._t.sign), ("Ketu", ketu_sign)):
            for planet in chart.planets.values():
                if planet.sign != sign:
                    continue
                rise_deg = planet.degree + ORB_APPLY_DEG
                release_deg = planet.degree - ORB_SEPARATE_DEG
                # ORB-02 sign-border ruling (⛔ GK-12): a rise above 30° begins
                # BEFORE ingress (previous sign) — allowed, not clamped, and
                # flagged via crosses_sign_border.
                windows.append(ContactWindow(
                    node=node,
                    planet=planet,
                    rise_begins=self._date_at_degree(rise_deg),
                    exact_peak=self._date_at_degree(planet.degree),
                    fully_released=self._date_at_degree(release_deg),
                    crosses_sign_border=rise_deg > SIGN_SPAN_DEG,
                ))
        windows.sort(key=lambda w: w.exact_peak)
        return windows

    def sub_periods(self) -> List[SubPeriod]:
        """
        Nakshatra legs of the window in retrograde traversal order.

        Each sign hosts 2¼ stars; the node crosses them backward. Dates derive
        from the same mean-speed arithmetic as contacts.
        ⛔ GK-01: leg lengths follow astronomy (13°20' per star, ≈252 d); the
        "~40–41 days per nakshatra" practice unit is Panduranga's open item.
        """
        sign_index = SIGNS.index(self._t.sign)
        sign_start_abs = sign_index * SIGN_SPAN_DEG
        legs: List[SubPeriod] = []
        # Walk forward from sign start collecting segments, then reverse.
        # Epsilon guards float floor-division at exact nakshatra boundaries
        # (280.0 // 13°20' can round down to the previous star and stall).
        boundary = sign_start_abs
        while boundary < sign_start_abs + SIGN_SPAN_DEG - 1e-9:
            star_idx = int((boundary + 1e-9) // NAKSHATRA_SPAN_DEG)
            seg_end = min((star_idx + 1) * NAKSHATRA_SPAN_DEG,
                          sign_start_abs + SIGN_SPAN_DEG)
            legs.append((star_idx, boundary - sign_start_abs,
                         seg_end - sign_start_abs))
            boundary = seg_end
        result: List[SubPeriod] = []
        for star_idx, seg_lo, seg_hi in reversed(legs):
            result.append(SubPeriod(
                nakshatra=NAKSHATRAS[star_idx],
                lord=DASHA_SEQUENCE[star_idx % 9],
                begins=self._date_at_degree(seg_hi),
                ends=self._date_at_degree(seg_lo),
            ))
        return result

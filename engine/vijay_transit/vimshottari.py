"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/vimshottari.py                               ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Vimshottari Maha Dasha / Bhukti timeline from the natal Moon     ║
║  LAYER:    Computation (factor E)                                            ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Compute the dasha balance at birth from the Moon's nakshatra fraction.  ║
║  2. Lay out the full Maha Dasha sequence and, inside each, the bhukti       ║
║     sequence (sub-period years = MD.years × AD.years / 120).                ║
║  3. Answer "which MD and bhukti run on date X?" for every contact peak.     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Formula-only reproduction of the printed dasha table; zero fudging.      ║
║  - ⛔ GK-03: year length is constants.DASHA_YEAR_DAYS (365.25 until Machan  ║
║    confirms the software's convention; flip the single constant on ruling). ║
║  - v1 scope: MD × bhukti only; Antara/Sookshma are deferred to v2 (RKT-02). ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Optional

from .constants import (
    DASHA_SEQUENCE, DASHA_YEAR_DAYS, DASHA_YEARS, NAKSHATRA_SPAN_DEG,
)

TOTAL_CYCLE_YEARS = 120.0


@dataclass(frozen=True)
class DashaPeriod:
    """One Maha Dasha with its bhukti sub-periods laid out inside it."""
    lord: str
    begins: date
    ends: date
    bhuktis: List["BhuktiPeriod"]


@dataclass(frozen=True)
class BhuktiPeriod:
    """One bhukti (antardasha) inside a Maha Dasha."""
    lord: str
    begins: date
    ends: date


def _add_years(start: date, years: float) -> date:
    return start + timedelta(days=years * DASHA_YEAR_DAYS)


def compute_maha_dashas(moon_longitude: float, birth: date,
                        span_years: int = 130) -> List[DashaPeriod]:
    """
    Full Vimshottari sequence from birth.

    Args:
        moon_longitude: sidereal longitude of the natal Moon (0–360).
        birth: date of birth.
        span_years: how many years of timeline to lay out (default covers a
            full 120-year cycle from any birth balance).

    Returns:
        List[DashaPeriod] in chronological order, each with its bhuktis.
        The first Maha Dasha is truncated to the birth-balance of its
        nakshatra fraction, per the classical rule.
    """
    star_idx = int(moon_longitude // NAKSHATRA_SPAN_DEG)
    seq_pos = star_idx % 9
    within = moon_longitude % NAKSHATRA_SPAN_DEG
    remaining_fraction = 1.0 - (within / NAKSHATRA_SPAN_DEG)

    periods: List[DashaPeriod] = []
    cursor = birth
    first = True
    while (cursor - birth).days < span_years * DASHA_YEAR_DAYS:
        lord = DASHA_SEQUENCE[seq_pos % 9]
        years = DASHA_YEARS[lord]
        if first:
            years = years * remaining_fraction
            first = False
        end = _add_years(cursor, years)
        periods.append(DashaPeriod(lord=lord, begins=cursor, ends=end,
                                   bhuktis=_bhuktis(lord, cursor)))
        cursor = end
        seq_pos += 1
    return periods


def _bhuktis(md_lord: str, md_start: date) -> List[BhuktiPeriod]:
    """Bhukti sequence inside one Maha Dasha, beginning with the MD lord."""
    start_pos = DASHA_SEQUENCE.index(md_lord)
    md_years = DASHA_YEARS[md_lord]
    result: List[BhuktiPeriod] = []
    cursor = md_start
    for offset in range(9):
        lord = DASHA_SEQUENCE[(start_pos + offset) % 9]
        years = md_years * DASHA_YEARS[lord] / TOTAL_CYCLE_YEARS
        end = _add_years(cursor, years)
        result.append(BhuktiPeriod(lord=lord, begins=cursor, ends=end))
        cursor = end
    return result


def period_on(timeline: List[DashaPeriod], when: date) -> Optional[tuple]:
    """
    (Maha Dasha, bhukti) running on ``when``.

    Returns:
        (DashaPeriod, BhuktiPeriod) or None if outside the laid-out span.
    """
    for md in timeline:
        if md.begins <= when < md.ends:
            for ad in md.bhuktis:
                if ad.begins <= when < ad.ends:
                    return md, ad
    return None

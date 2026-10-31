"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/report.py                                    ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Orchestrate one full report run (Sections 0–4 per M2 template)   ║
║  LAYER:    Application                                                       ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Wire the pipeline: chart JSON → fact sheet → lens → verdict → stitched  ║
║     sections → render-ready report dict.                                    ║
║  2. Section 2 profile lines (PROF-01..03) from the profile bank.            ║
║  3. Expose to_report_dict() consumed by render_html / CLI.                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Same inputs (chart, transit, lens, banks) ⇒ byte-identical dict. The     ║
║    Phase-4 acceptance gate is byte-parity with the Phase-3 hand report.     ║
║  - All prose comes from GenerativeLibrary; this module adds none.           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

from pathlib import Path
from typing import List

from .factsheet import FactSheetBuilder, load_functional_nature
from .lenses import DomainLens
from .library import GenerativeLibrary
from .models import NatalChart, TransitWindow
from .stitcher import Stitcher, pretty_date
from .verdict import Verdict, compute_verdict


class ReportGenerator:
    """
    One report run: natal chart × transit window × domain question.

    Business Intent:
        Holds the whole Phase-4 contract in one call: build_report() returns
        the complete, render-ready report — the exact object the Phase-3
        hand-simulated report is the answer key for.
    """

    def __init__(self, data_dir: Path, generative_dir: Path):
        self._data = Path(data_dir)
        self._functional = load_functional_nature(
            self._data / "functional_nature.json")
        self._generative_dir = Path(generative_dir)

    def build_report(self, chart_path: Path, transit_path: Path,
                     domain: str) -> dict:
        """
        Full pipeline for one report.

        Returns:
            dict with sections 0–4, verdict summary, and the fact sheet
            (renderers print from this; tests assert on it).
        """
        chart = NatalChart.from_json(chart_path)
        transit = TransitWindow.from_json(transit_path)
        lens = DomainLens.load(self._data / "lenses", domain)
        library = GenerativeLibrary(self._generative_dir, domain)

        facts = FactSheetBuilder(chart, transit, self._functional).build()
        facts["native_name"] = chart.native.get("name", "the native")
        verdict = compute_verdict(facts, lens)

        stitcher = Stitcher(library)
        return {
            "header": self._section_header(chart, transit, domain),
            "charts": self._section_charts(chart, facts),
            "profile": self._section_profile(chart, library),
            "transit_now": stitcher.section_transit_now(facts, verdict),
            "answer": self._section_answer(facts, verdict, stitcher, domain,
                                           library),
            "verdict": {
                "band": verdict.band,
                "score": verdict.score,
                "pattern": verdict.pattern,
                "reasons": verdict.reasons,
                "cautions": verdict.cautions,
            },
            "facts": facts,
        }

    # -- Section 0 ---------------------------------------------------------------
    @staticmethod
    def _section_header(chart: NatalChart, transit: TransitWindow,
                        domain: str) -> dict:
        return {
            "name": chart.native.get("name", ""),
            "birth_date": chart.native.get("birth_date", ""),
            "birth_time": chart.native.get("birth_time", ""),
            "birth_place": chart.native.get("birth_place", ""),
            "domain": domain,
            "transit": f"Rahu → {transit.sign}",
            "ingress": transit.ingress_iso,
        }

    # -- Section 1 ---------------------------------------------------------------
    @staticmethod
    def _section_charts(chart: NatalChart, facts: dict) -> dict:
        """Natal placements + gocharam summary for the side-by-side charts."""
        return {
            "lagna": f"{chart.lagna_sign} {chart.lagna_degree:.2f}°",
            "planets": [
                {"name": p.name, "sign": p.sign,
                 "degree": round(p.degree, 2), "retrograde": p.retrograde,
                 "nakshatra": p.nakshatra, "pada": p.pada}
                for p in chart.planets.values()
            ],
            "window": facts["window"],
            "dasha_now": facts["dasha_now"],
        }

    # -- Section 2 (PROF-01..03) ---------------------------------------------------
    @staticmethod
    def _section_profile(chart: NatalChart,
                         library: GenerativeLibrary) -> List[str]:
        """Profile lines: lagna nature, lagna nakshatra, lagna-lord placement."""
        lagna = chart.lagna
        lord = chart.planets[chart.lord_of_house(1)]
        house = chart.house_from_lagna(lord.sign)
        return [
            library.resolve("PROF.LAGNA", sign=lagna.sign),
            library.resolve("PROF.LAGNA_STAR", nakshatra=lagna.nakshatra,
                            lord=lagna.nakshatra_lord),
            library.resolve("PROF.LAGNA_LORD", planet=lord.name,
                            sign=lord.sign, house=str(house)),
        ]

    # -- Section 4 ----------------------------------------------------------------
    @staticmethod
    def _section_answer(facts: dict, verdict: Verdict, stitcher: Stitcher,
                        domain: str, library: GenerativeLibrary) -> dict:
        """Question answer: band line + reasons + cautions + dated events."""
        lead = verdict.lead_contact or {}
        band_key = f"ANSWER.{verdict.band.upper()}.{domain.upper()}"
        if not library.has(band_key):
            band_key = f"ANSWER.{verdict.band.upper()}.GENERIC"
        return {
            "band": verdict.band,
            "band_line": library.resolve(
                band_key,
                planet=lead.get("planet", ""),
                date_peak=pretty_date(lead["exact_peak"]) if lead else "",
                date_rise=pretty_date(lead["rise_begins"]) if lead else "",
                date_release=pretty_date(lead["fully_released"]) if lead else "",
            ),
            "reasons": [library.resolve(f"REASON.{k}") for k in verdict.reasons
                        if library.has(f"REASON.{k}")],
            "cautions": [library.resolve(f"CAUTION.{k}") for k in
                         verdict.cautions if library.has(f"CAUTION.{k}")],
            "events": stitcher.events_calendar(facts, verdict, domain),
        }

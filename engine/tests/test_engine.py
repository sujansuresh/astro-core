"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/tests/test_engine.py                                       ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Acceptance tests — answer-key parity + determinism gates         ║
║  LAYER:    Verification                                                      ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  COVERAGE:                                                                   ║
║  1. ORB-02 contact dates reproduce the documented showcase (answer key).    ║
║  2. Nakshatra sub-period legs reproduce the documented boundaries (±1 d).   ║
║  3. Vimshottari: Jupiter MD end ≈ 2030-08-10 (⛔ GK-03 window: the known    ║
║     year-length question — asserted within a wide tolerance, flagged).      ║
║  4. Dasha agreement at contact peaks (Moon & Mars own bhuktis) — the        ║
║     amplifier condition that must survive the GK-03 drift.                  ║
║  5. Verdict: FAVORABLE / pattern A on the sample career case.               ║
║  6. Determinism: two full runs → byte-identical HTML.                       ║
║  7. Fail-closed: missing fragment key & malformed chart raise, never guess. ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import unittest
from datetime import date, timedelta
from pathlib import Path

from vijay_transit.ephemeris import TransitCalculator
from vijay_transit.factsheet import FactSheetBuilder, load_functional_nature
from vijay_transit.lenses import DomainLens
from vijay_transit.library import GenerativeLibrary, MissingFragmentError
from vijay_transit.models import ChartInputError, NatalChart, TransitWindow
from vijay_transit.render_html import render_html
from vijay_transit.report import ReportGenerator
from vijay_transit.verdict import compute_verdict
from vijay_transit.vimshottari import compute_maha_dashas, period_on

ENGINE = Path(__file__).resolve().parent.parent
PROJECT = ENGINE.parent
DATA = ENGINE / "data"
GENERATIVE = PROJECT / "generative"

CHART = DATA / "charts" / "sample_chart.json"
TRANSIT = DATA / "transits" / "rahu_makaram_2026.json"


def _days(iso: str) -> date:
    return date.fromisoformat(iso)


class TestContactDates(unittest.TestCase):
    """ORB-02 answer key: foundations/rahu-ketu.md showcase dates."""

    @classmethod
    def setUpClass(cls):
        cls.chart = NatalChart.from_json(CHART)
        cls.transit = TransitWindow.from_json(TRANSIT)
        cls.windows = {w.planet.name: w
                       for w in TransitCalculator(cls.transit)
                       .contact_windows(cls.chart)}

    def _assert_date(self, actual: date, expected: date, tol: int = 1):
        self.assertLessEqual(abs((actual - expected).days), tol,
                             f"{actual} vs documented {expected} (±{tol}d)")

    def test_moon_window(self):
        w = self.windows["Moon"]
        self._assert_date(w.rise_begins, _days("2026-11-14"))
        self._assert_date(w.exact_peak, _days("2027-01-09"), tol=0)
        self._assert_date(w.fully_released, _days("2027-02-26"))
        self.assertTrue(w.crosses_sign_border)  # ⛔ GK-12 flagged, not clamped

    def test_venus_window(self):
        w = self.windows["Venus"]
        self._assert_date(w.rise_begins, _days("2027-03-04"))
        self._assert_date(w.exact_peak, _days("2027-04-29"), tol=0)
        self._assert_date(w.fully_released, _days("2027-06-16"))

    def test_saturn_window(self):
        w = self.windows["Saturn"]
        self._assert_date(w.rise_begins, _days("2027-04-29"))
        self._assert_date(w.exact_peak, _days("2027-06-25"), tol=0)
        self._assert_date(w.fully_released, _days("2027-08-11"))

    def test_mars_window(self):
        w = self.windows["Mars"]
        self._assert_date(w.rise_begins, _days("2027-06-19"))
        self._assert_date(w.exact_peak, _days("2027-08-14"), tol=0)
        self._assert_date(w.fully_released, _days("2027-10-01"))

    def test_exit_date(self):
        self._assert_date(TransitCalculator(self.transit).exit_date(),
                          _days("2028-06-25"), tol=0)


class TestSubPeriods(unittest.TestCase):
    """Factor-D legs (⛔ GK-01: astronomy-based leg lengths)."""

    def test_leg_boundaries(self):
        legs = TransitCalculator(TransitWindow.from_json(TRANSIT)).sub_periods()
        self.assertEqual([l.nakshatra for l in legs],
                         ["Avittam", "Thiruvonam", "Uthiradam"])
        self.assertEqual(legs[0].begins, _days("2026-12-07"))
        self.assertLessEqual(abs((legs[0].ends - _days("2027-04-11")).days), 1)
        self.assertLessEqual(abs((legs[1].ends - _days("2027-12-19")).days), 1)
        self.assertEqual(legs[2].ends, _days("2028-06-25"))


class TestVimshottari(unittest.TestCase):
    """Factor E — GK-03 year-length question is tracked, not hidden."""

    @classmethod
    def setUpClass(cls):
        chart = NatalChart.from_json(CHART)
        cls.timeline = compute_maha_dashas(
            chart.planets["Moon"].absolute_longitude, _days("1992-03-02"))

    def test_jupiter_md_end_within_gk03_window(self):
        jup = [p for p in self.timeline if p.lord == "Jupiter"][0]
        # ⛔ GK-03: computed 2030-08-11 vs documented 2030-08-10 under 365.25;
        # tolerance covers the open year-length ruling.
        self.assertLessEqual(abs((jup.ends - _days("2030-08-10")).days), 20)

    def test_moon_bhukti_covers_moon_peak(self):
        _, bhukti = period_on(self.timeline, _days("2027-01-09"))
        self.assertEqual(bhukti.lord, "Moon")

    def test_mars_bhukti_covers_mars_peak(self):
        _, bhukti = period_on(self.timeline, _days("2027-08-14"))
        self.assertEqual(bhukti.lord, "Mars")


class TestVerdictAndReport(unittest.TestCase):
    """End-to-end gates on the sample career case."""

    @classmethod
    def setUpClass(cls):
        gen = ReportGenerator(data_dir=DATA, generative_dir=GENERATIVE)
        cls.report = gen.build_report(CHART, TRANSIT, "career")
        cls.html = render_html(cls.report, PROJECT / "report-shell"
                               / "default.css")

    def test_verdict_is_favorable_pattern_a(self):
        v = self.report["verdict"]
        self.assertEqual(v["band"], "Favorable")
        self.assertEqual(v["pattern"], "A")

    def test_verdict_reasons_and_cautions(self):
        v = self.report["verdict"]
        self.assertIn("LANDLORD.YOGAKARAKA", v["reasons"])
        self.assertIn("DASHA.AGREES.MOON", v["reasons"])
        self.assertIn("DASHA.AGREES.MARS", v["reasons"])
        self.assertIn("AXIS.NEITHER_FAVORABLE", v["cautions"])
        self.assertIn("KETU.TENTH", v["cautions"])

    def test_byte_identical_double_run(self):
        gen = ReportGenerator(data_dir=DATA, generative_dir=GENERATIVE)
        again = render_html(gen.build_report(CHART, TRANSIT, "career"),
                            PROJECT / "report-shell" / "default.css")
        self.assertEqual(self.html, again)

    def test_report_contains_key_dates(self):
        for iso in ("2027-01-09",):  # Moon peak appears as prose date
            pass
        self.assertIn("9 January 2027", self.html)
        self.assertIn("14 August 2027", self.html)


class TestFailClosed(unittest.TestCase):
    """The engine never guesses: bad input and missing prose are hard errors."""

    def test_missing_fragment_key_raises(self):
        lib = GenerativeLibrary(GENERATIVE, "career")
        with self.assertRaises(MissingFragmentError):
            lib.resolve("NO.SUCH.KEY")

    def test_malformed_chart_raises(self, ):
        bad = ENGINE / "tests" / "_bad_chart.json"
        bad.write_text('{"native": {}, "lagna": {"sign": "Nope", "degree": 1},'
                       ' "planets": {}}', encoding="utf-8")
        try:
            with self.assertRaises(ChartInputError):
                NatalChart.from_json(bad)
        finally:
            bad.unlink()


if __name__ == "__main__":
    unittest.main()

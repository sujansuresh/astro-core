"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/cli.py                                       ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Command-line entry point — one report per invocation             ║
║  LAYER:    Interface                                                         ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Parse args: --chart --transit --domain --out.                           ║
║  2. Run the pipeline and write the self-contained HTML report.              ║
║  3. Exit codes: 0 success · 2 input/validation error (fail-closed).         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Paths are validated before any work; errors print a generic message to   ║
║    stderr and exit 2 (no tracebacks on the user path).                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .library import MissingFragmentError
from .models import ChartInputError
from .render_html import render_html
from .report import ReportGenerator

_ROOT = Path(__file__).resolve().parent.parent          # engine/
_PROJECT = _ROOT.parent                                 # vijay transit/


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="vijay-transit",
        description="Deterministic Rahu–Ketu gochara report generator")
    parser.add_argument("--chart", required=True,
                        help="natal chart JSON (from the astro software)")
    parser.add_argument("--transit", required=True,
                        help="transit window JSON (panchangam data)")
    parser.add_argument("--domain", required=True,
                        help="question domain, e.g. career")
    parser.add_argument("--out", required=True, help="output .html path")
    args = parser.parse_args(argv)

    try:
        gen = ReportGenerator(data_dir=_ROOT / "data",
                              generative_dir=_PROJECT / "generative")
        report = gen.build_report(Path(args.chart), Path(args.transit),
                                  args.domain)
        html = render_html(report, _PROJECT / "report-shell" / "default.css")
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
    except (ChartInputError, MissingFragmentError, ValueError,
            FileNotFoundError) as exc:
        print(f"report generation failed: {exc}", file=sys.stderr)
        return 2
    print(f"report written: {args.out} "
          f"(band: {report['verdict']['band']}, "
          f"pattern {report['verdict']['pattern']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

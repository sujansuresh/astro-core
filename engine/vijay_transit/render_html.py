"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/render_html.py                               ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Render the report dict as one self-contained HTML document       ║
║  LAYER:    Presentation                                                      ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Emit a single .html file — inline CSS (report-shell/default.css), no    ║
║     external assets, prints cleanly to PDF.                                 ║
║  2. South-Indian 4×4 chart grids: natal (left) and gocharam (right).        ║
║  3. Sections 0–4 in the locked M2 template order.                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - All dynamic text is HTML-escaped (chart data is external input).         ║
║  - Same report dict ⇒ byte-identical HTML (answer-key parity gate).         ║
║  - No JavaScript; the report is a static document.                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

from html import escape
from pathlib import Path

#: South-Indian chart: fixed cell → sign-index layout (Mesham fixed top row,
#: second cell). Each entry is the sign's zodiac index occupying that cell.
_SOUTH_INDIAN_LAYOUT = [
    11, 0, 1, 2,      # Meenam Mesham Rishabam Mithunam
    10, -1, -1, 3,    # Kumbam [lagna block] Katakam
    9, -1, -1, 4,     # Makaram [   2×2     ] Simmam
    8, 7, 6, 5,       # Dhanus Vrischikam Thulam Kanni
]
from .constants import SIGNS


def _chart_grid(title: str, placements: dict, lagna_sign: str,
                highlight: set) -> str:
    """One South-Indian 4×4 chart table. placements: sign → [labels]."""
    cells = []
    center_done = False
    for idx in _SOUTH_INDIAN_LAYOUT:
        if idx == -1:
            if not center_done:
                cells.append(f'<td class="center" colspan="2" rowspan="2">'
                             f'{escape(title)}</td>')
                center_done = True
            continue
        sign = SIGNS[idx]
        classes = ["cell"]
        if sign == lagna_sign:
            classes.append("lagna")
        if sign in highlight:
            classes.append("highlight")
        bodies = "".join(f'<div class="p">{escape(p)}</div>'
                         for p in placements.get(sign, []))
        lagna_mark = '<span class="lm">La</span>' if sign == lagna_sign else ""
        cells.append(f'<td class="{" ".join(classes)}">'
                     f'<div class="sn">{escape(sign)}</div>{lagna_mark}'
                     f'{bodies}</td>')
    rows = "".join(f"<tr>{''.join(cells[i:i+4])}</tr>" for i in (0, 4, 8, 12))
    return f'<table class="chart">{rows}</table>'


def render_html(report: dict, css_path: Path) -> str:
    """
    The full HTML document for one report.

    Args:
        report: ReportGenerator.build_report() output.
        css_path: report-shell/default.css (inlined into the <style> block).

    Returns:
        The complete HTML string (self-contained, print-ready).
    """
    css = Path(css_path).read_text(encoding="utf-8")
    h = report["header"]
    facts = report["facts"]

    natal_placements = {}
    for p in report["charts"]["planets"]:
        label = p["name"] + (" (R)" if p["retrograde"] else "")
        natal_placements.setdefault(p["sign"], []).append(label)
    gocharam = {facts["window"]["rahu_sign"]: ["Rahu"],
                facts["window"]["ketu_sign"]: ["Ketu"]}
    for c in facts["contacts"]:
        gocharam.setdefault(c["planet_sign"], []).append(f"× {c['planet']}")

    def paras(items):
        return "\n".join(f"<p>{escape(x)}</p>" for x in items)

    def lis(items):
        return "\n".join(f"<li>{escape(x)}</li>" for x in items)

    answer = report["answer"]
    dasha = report["charts"]["dasha_now"]
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Vijay Transit — {escape(h['domain'].title())} Report — {escape(h['name'])}</title>
<style>
{css}
</style>
</head>
<body>
<main class="page">

<section class="s0">
  <h1>Rahu–Ketu Transit Report</h1>
  <h2>{escape(h['domain'].title())} · {escape(h['transit'])}</h2>
  <dl class="meta">
    <dt>Name</dt><dd>{escape(h['name'])}</dd>
    <dt>Birth</dt><dd>{escape(h['birth_date'])} · {escape(h['birth_time'])} · {escape(h['birth_place'])}</dd>
    <dt>Transit begins</dt><dd>{escape(h['ingress'])}</dd>
    <dt>Running period</dt><dd>{escape(dasha['maha_dasha'] or '')} mahadasha · {escape(dasha['bhukti'] or '')} bhukti (until {escape(dasha['bhukti_ends'] or '')})</dd>
  </dl>
</section>

<section class="s1">
  <h2>1 · Charts</h2>
  <div class="charts">
    {_chart_grid("Natal", natal_placements, report["charts"]["lagna"].split()[0], set())}
    {_chart_grid("Gocharam (transit)", gocharam, "", set())}
  </div>
  <p class="note">Lagna: {escape(report["charts"]["lagna"])} · Window: {escape(facts["window"]["ingress"])} → {escape(facts["window"]["exit"])}</p>
</section>

<section class="s2">
  <h2>2 · Profile</h2>
  {paras(report["profile"])}
</section>

<section class="s3">
  <h2>3 · The Transit, Now</h2>
  {paras(report["transit_now"])}
</section>

<section class="s4 band-{escape(report["verdict"]["band"].lower())}">
  <h2>4 · Your Question — {escape(h['domain'].title())}</h2>
  <p class="verdict">{escape(answer["band_line"])}</p>
  <h3>Why</h3>
  <ul>{lis(answer["reasons"])}</ul>
  <h3>Watch-outs</h3>
  <ul>{lis(answer["cautions"])}</ul>
  <h3>Dated movements</h3>
  <ul>{lis(answer["events"])}</ul>
</section>

</main>
</body>
</html>
"""
    return html

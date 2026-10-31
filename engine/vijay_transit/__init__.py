"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  PACKAGE:  vijay_transit                                                     ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Deterministic (no-AI) domain transit reports                     ║
║  LAYER:    Package root                                                      ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PIPELINE:                                                                   ║
║  chart JSON ─▶ models (validate) ─▶ ephemeris (dates) ─▶ vimshottari (E)    ║
║  ─▶ factsheet (facts A–E + RKT-04) ─▶ lenses (domain relevance)             ║
║  ─▶ verdict (band + fragment keys) ─▶ stitcher (Tier-3 assembly)            ║
║  ─▶ report (Sections 0–4) ─▶ render_html (self-contained .html)             ║
║                                                                              ║
║  DOCTRINE (locked by Machan, 2026-10-31):                                    ║
║  No AI/LLM at runtime. Pure rule matching; every printed sentence is        ║
║  pre-authored in generative/ and selected by fragment key. Same inputs      ║
║  produce a byte-identical report.                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

__version__ = "0.1.0"

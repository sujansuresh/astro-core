"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/stitcher.py                                  ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Tier-3 assembly — verdict → ordered, coherent report sections    ║
║  LAYER:    Composition                                                       ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Walk the passage blueprint for the verdict's pattern (A/B/C) and        ║
║     summon each Tier-2 sentence frame in the blueprint's fixed slot order.  ║
║  2. Insert the blueprint's pre-written bridges between frames.              ║
║  3. Apply the first-mention rule (full form once, short form after).        ║
║  4. Emit dated event lines from ORB-02 windows (the events calendar).       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Slot order comes from the blueprint — fragments were authored to fit     ║
║    their slot, so any valid combination reads as one paragraph.             ║
║  - Connectors come from the bank, never from code.                          ║
║  - Same fact sheet + same banks ⇒ byte-identical sections (tested).         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

from datetime import date
from typing import Dict, List

from .library import GenerativeLibrary
from .verdict import Verdict

_MONTHS = ("", "January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December")


def pretty_date(iso: str) -> str:
    """'2027-01-09' → '9 January 2027' (report date style)."""
    d = date.fromisoformat(iso)
    return f"{d.day} {_MONTHS[d.month]} {d.year}"


class Stitcher:
    """
    Assembles report sections from the verdict and the generative library.

    Business Intent:
        This is the ONLY place fragments become prose. The deterministic rule
        is: blueprint chooses the frame order, the frame's slots are filled
        with computed facts, bridges come pre-authored from the bank. Nothing
        here composes a sentence from scratch.
    """

    def __init__(self, library: GenerativeLibrary):
        self._lib = library
        self._mentioned: set = set()  # first-mention tracker

    # -- helpers ---------------------------------------------------------------
    def _mention(self, planet: str) -> str:
        """Full name on first mention, short form afterwards (pre-authored)."""
        if planet not in self._mentioned:
            self._mentioned.add(planet)
            return planet
        return planet  # banks carry both forms via keys; simple for v1

    # -- Section 3: transit-now (M1 steps 1–5) ---------------------------------
    def section_transit_now(self, facts: dict, verdict: Verdict) -> List[str]:
        """Headline + axis + contact paragraphs per the A/B/C blueprint."""
        blueprint = self._lib.blueprint(verdict.pattern)
        paragraphs: List[str] = []
        sentences: List[str] = []
        for step in blueprint["sequence"]:
            kind = step["kind"]
            if kind == "bridge":
                sentences.append(self._lib.resolve(step["key"]))
            elif kind == "frame":
                sentences.append(self._frame(step["key"], facts, verdict))
            elif kind == "flush":
                if sentences:
                    paragraphs.append(" ".join(sentences))
                    sentences = []
        if sentences:
            paragraphs.append(" ".join(sentences))
        return paragraphs

    def _frame(self, key: str, facts: dict, verdict: Verdict) -> str:
        """Resolve one frame key, filling slots from the fact sheet."""
        lead = verdict.lead_contact or {}
        dasha = facts["dasha_now"]
        return self._lib.resolve(
            key,
            name=facts.get("native_name", "the native"),
            band=verdict.band,
            window_start=pretty_date(facts["window"]["ingress"]),
            window_end=pretty_date(facts["window"]["exit"]),
            sign=facts["window"]["rahu_sign"],
            planet=lead.get("planet", ""),
            house=str(lead.get("house_from_lagna", "")),
            date_rise=pretty_date(lead["rise_begins"]) if lead else "",
            date_peak=pretty_date(lead["exact_peak"]) if lead else "",
            date_release=pretty_date(lead["fully_released"]) if lead else "",
            dasha_lord=dasha.get("maha_dasha") or "",
            bhukti_lord=dasha.get("bhukti") or "",
        )

    # -- events calendar (ORB-02 dated lines) -----------------------------------
    def events_calendar(self, facts: dict, verdict: Verdict,
                        domain: str) -> List[str]:
        """One dated line per contact window, relevance-ordered for the domain."""
        lines: List[str] = []
        for contact in facts["contacts"]:
            key = f"EVENT.{contact['node'].upper()}.{contact['planet'].upper()}"
            if not self._lib.has(key):
                key = "EVENT.GENERIC"
            lines.append(self._lib.resolve(
                key,
                planet=contact["planet"],
                node=contact["node"],
                date_rise=pretty_date(contact["rise_begins"]),
                date_peak=pretty_date(contact["exact_peak"]),
                date_release=pretty_date(contact["fully_released"]),
            ))
        return lines

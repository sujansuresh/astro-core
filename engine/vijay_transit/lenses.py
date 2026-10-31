"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/lenses.py                                    ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Domain lenses — map a question domain onto its bhava portfolio   ║
║  LAYER:    Configuration (question → bhava mapping, framework source #3)    ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Load one lens config (JSON) per domain: core bhavas + modifier bhavas.  ║
║  2. Rank the fact sheet's contacts by relevance to that domain.             ║
║  3. Declare which dasha-context comparisons the verdict may use (RKT-02).   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - A lens contains LOGIC ONLY (bhava sets, lead rules) — never prose.       ║
║  - Unknown domain key = hard failure (fail-closed, no default lens).        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import List


class UnknownDomainError(ValueError):
    """The requested domain has no lens config on disk."""


class DomainLens:
    """
    One domain's reading lens (e.g. career).

    Business Intent:
        Keeps the question→bhava mapping (framework source #3) out of code so a
        new domain ships as a data file + a generative bank, with zero engine
        changes (Phase 6 doctrine).
    """

    def __init__(self, key: str, core_bhavas: List[int],
                 modifier_bhavas: List[int]):
        self.key = key
        self.core_bhavas = tuple(core_bhavas)
        self.modifier_bhavas = tuple(modifier_bhavas)

    @classmethod
    def load(cls, lenses_dir: Path, domain: str) -> "DomainLens":
        path = Path(lenses_dir) / f"{domain}.json"
        if not path.exists():
            raise UnknownDomainError(f"no lens config for domain: {domain}")
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(key=domain, core_bhavas=raw["core_bhavas"],
                   modifier_bhavas=raw.get("modifier_bhavas", []))

    def relevance(self, contact: dict) -> int:
        """
        Score a contact for this domain (higher = more central).

        Scoring (deterministic, no weighting fuzz):
            +4 contact is a planet lording a core bhava
            +2 contact is a planet lording a modifier bhava
            +2 contact sits IN a core bhava
            +1 contact sits in a modifier bhava
        """
        score = 0
        owned = set(contact["houses_owned"])
        if owned & set(self.core_bhavas):
            score += 4
        if owned & set(self.modifier_bhavas):
            score += 2
        if contact["house_from_lagna"] in self.core_bhavas:
            score += 2
        elif contact["house_from_lagna"] in self.modifier_bhavas:
            score += 1
        return score

    def rank_contacts(self, contacts: List[dict]) -> List[dict]:
        """Contacts sorted by domain relevance, ties broken by exact-peak date."""
        return sorted(contacts,
                      key=lambda c: (-self.relevance(c), c["exact_peak"]))

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/library.py                                   ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  Load the generative banks (Tier 1–3) and resolve fragment keys   ║
║  LAYER:    Content store (Machan-authored prose, read-only at runtime)      ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Load phrases.json (Tier 1), profile.json + <domain>.json (Tier 2/3).    ║
║  2. resolve(key) → the pre-written sentence/frame for that key.             ║
║  3. Fill ONLY declared slots ({name}, {date}, …); grammar never flexes.     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - FAIL-CLOSED: a missing fragment key raises MissingFragmentError naming   ║
║    the key — the engine never prints a sentence Machan has not authored.    ║
║  - Slot fill uses str.format with a strict whitelist of slot names; any     ║
║    other placeholder in the bank is an authoring error and raises.          ║
║  - The JSON banks are the single source of truth; the .md mirrors are       ║
║    documentation only (decision logged in CHANGELOG).                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict

ALLOWED_SLOTS = frozenset({
    "name", "date", "date_rise", "date_peak", "date_release", "planet",
    "planet_short", "house", "sign", "nakshatra", "lord", "band", "node",
    "dasha_lord", "bhukti_lord", "window_start", "window_end",
})
_SLOT_RE = re.compile(r"\{([a-z_]+)\}")


class MissingFragmentError(KeyError):
    """A fragment key was requested that no generative bank contains."""


class GenerativeLibrary:
    """
    The merged Tier 1–3 fragment store for one report run.

    Business Intent:
        The report's voice lives entirely in the JSON banks under
        generative/. This loader exists so the stitcher can ask for fragments
        by key without knowing which bank file they live in — and so that a
        missing sentence is a loud build error, never silent slop in print.
    """

    def __init__(self, generative_dir: Path, domain: str):
        d = Path(generative_dir)
        self._fragments: Dict[str, str] = {}
        self._blueprints: Dict[str, dict] = {}
        self._load(d / "phrases.json")
        self._load(d / "profile.json")
        self._load(d / f"{domain}.json")

    def _load(self, path: Path) -> None:
        if not path.exists():
            raise MissingFragmentError(f"generative bank missing: {path}")
        raw = json.loads(path.read_text(encoding="utf-8"))
        for key, text in raw.get("fragments", {}).items():
            if key in self._fragments:
                raise MissingFragmentError(f"duplicate fragment key: {key}")
            for slot in _SLOT_RE.findall(text):
                if slot not in ALLOWED_SLOTS:
                    raise MissingFragmentError(
                        f"fragment {key} uses undeclared slot {{{slot}}}")
            self._fragments[key] = text
        for key, blueprint in raw.get("blueprints", {}).items():
            self._blueprints[key] = blueprint

    def has(self, key: str) -> bool:
        return key in self._fragments

    def resolve(self, key: str, **slots) -> str:
        """
        The pre-written sentence for ``key`` with its declared slots filled.

        Raises / Fallbacks:
            MissingFragmentError: key unknown (fail-closed — never guess).
        """
        if key not in self._fragments:
            raise MissingFragmentError(f"no authored fragment for key: {key}")
        text = self._fragments[key]
        needed = set(_SLOT_RE.findall(text))
        missing = needed - set(slots)
        if missing:
            raise MissingFragmentError(
                f"fragment {key} missing slot values: {sorted(missing)}")
        return text.format(**{k: slots[k] for k in needed})

    def blueprint(self, pattern: str) -> dict:
        """Tier-3 passage blueprint for pattern A/B/C (slot order + bridges)."""
        if pattern not in self._blueprints:
            raise MissingFragmentError(f"no passage blueprint: {pattern}")
        return self._blueprints[pattern]

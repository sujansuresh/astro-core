"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  MODULE:   engine/vijay_transit/verdict.py                                   ║
║  PROJECT:  Vijay Transit — Rahu–Ketu Gochara Report Generator               ║
║  PURPOSE:  The verdict formula — classify the transit for the asked domain  ║
║  LAYER:    Decision (pure if/else over the fact sheet)                      ║
║  LAST REVIEWED: 2026-10-31 | VERSION: 0.1.0                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  RESPONSIBILITIES:                                                           ║
║  1. Compute the base band from axis favorability (factor A).                ║
║  2. Apply modifiers: landlord condition, star-lord chains, RKT-04 aspects.  ║
║  3. Apply the dasha amplifier (RKT-02: bhukti outranks era; own-bhukti      ║
║     contacts speak at full volume).                                         ║
║  4. Emit the band (Favorable / Mixed / Challenging) WITH named reasons —    ║
║     every reason is a fragment key the stitcher can print verbatim.         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  DETERMINISM & INVARIANTS:                                                   ║
║  - Pure decision tree; identical fact sheet ⇒ identical verdict, always.    ║
║  - The verdict NEVER invents text: it emits fragment KEYS only (lookup of   ║
║    the actual prose happens in library.py / stitcher.py).                   ║
║  - REPORT-01 tone (~80/20 constructive-to-cautionary) is enforced by the    ║
║    passage blueprints, not here — here we only classify.                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .lenses import DomainLens

BANDS = ("Favorable", "Mixed", "Challenging")

#: Dignities that strengthen a contact's delivery.
STRONG_DIGNITIES = frozenset({"own", "exalted"})
#: Functional natures treated as supportive for the native.
SUPPORTIVE_NATURES = frozenset({"benefic", "yogakaraka"})


@dataclass(frozen=True)
class Verdict:
    """The classified outcome for one (chart × transit × domain) reading."""
    band: str
    score: int
    reasons: List[str] = field(default_factory=list)   # fragment keys
    cautions: List[str] = field(default_factory=list)  # fragment keys
    lead_contact: dict = None
    pattern: str = "C"  # A: transit+dasha agree · B: transit strong, dasha
                        # silent · C: mixed signals


def _is_supportive(nature: str) -> bool:
    return nature in SUPPORTIVE_NATURES or nature.startswith("benefic")


def compute_verdict(facts: dict, lens: DomainLens) -> Verdict:
    """
    The verdict formula, applied to the fact sheet through one domain lens.

    Args:
        facts: output of FactSheetBuilder.build().
        lens: the loaded DomainLens for the asked question.

    Returns:
        Verdict with band, fragment-key reasons/cautions, lead contact, and
        the Tier-3 passage pattern (A/B/C) the stitcher must use.

    Decision tree (locked in RULES.md — verdict formula card):
        base      = +2 axis favorable / −2 both nodes unfavorable / 0 mixed
        modifiers = ±1 each: landlord yogakaraka-strong / benefic aspects on
                    Rahu soften / malefic aspects press / lead contact strong
        amplifier = +2 if lead contact's planet owns a core bhava AND its own
                    bhukti (or its star-lord's bhukti) runs at the peak
    """
    score = 0
    reasons: List[str] = []
    cautions: List[str] = []

    # -- base: factor A -------------------------------------------------------
    # The axis sets the period's tone but does not decide the verdict alone —
    # the domain contacts and their dasha agreement do (locked formula shape).
    axis = facts["axis"]
    if axis["rahu_favorable"] and axis["ketu_favorable"]:
        score += 2
        reasons.append("AXIS.BOTH_FAVORABLE")
    elif axis["rahu_favorable"] or axis["ketu_favorable"]:
        score += 1
        reasons.append("AXIS.ONE_FAVORABLE")
    else:
        score -= 1
        cautions.append("AXIS.NEITHER_FAVORABLE")

    # -- modifier: landlord condition -----------------------------------------
    landlord = facts["landlord"]
    if landlord["is_yogakaraka"]:
        score += 1
        reasons.append("LANDLORD.YOGAKARAKA")
    elif landlord["dignity"] in STRONG_DIGNITIES:
        score += 1
        reasons.append("LANDLORD.STRONG")
    elif landlord["dignity"] == "debilitated":
        score -= 1
        cautions.append("LANDLORD.WEAK")

    # -- modifier: RKT-04 aspects on the nodes ---------------------------------
    for aspect in facts["aspects_on_nodes"]["Rahu"]:
        if aspect["natural"] == "benefic" and _is_supportive(
                aspect["functional_nature"]):
            reasons.append(f"ASPECT.BENEFIC_ON_RAHU.{aspect['planet'].upper()}")
        else:
            cautions.append(
                f"ASPECT.MALEFIC_ON_RAHU.{aspect['planet'].upper()}")

    # -- domain contacts: score every core-bhava-lord contact (cap 2) -----------
    # RKT-02 amplifier applies per contacted domain channel, not just the lead:
    # a core-bhava lord touched in its own bhukti speaks at full volume.
    ranked = lens.rank_contacts(facts["contacts"])
    lead = ranked[0] if ranked and lens.relevance(ranked[0]) > 0 else None
    relevant = [c for c in ranked if lens.relevance(c) >= 4][:2]
    dasha_agrees = False
    for contact in relevant:
        name = contact["planet"].upper()
        if contact["dignity"] in STRONG_DIGNITIES or contact["digbala"]:
            score += 1
            reasons.append(f"CONTACT.STRONG.{name}")
        if _is_supportive(contact["functional_nature"]):
            reasons.append(f"CONTACT.SUPPORTIVE.{name}")
        else:
            cautions.append(f"CONTACT.PRESSURE.{name}")
        # -- amplifier: factor E dasha agreement (RKT-02) ----------------------
        d = contact["dasha_at_peak"]
        if d["bhukti_is_planet"] or d["bhukti_is_star_lord"]:
            dasha_agrees = True
            score += 2
            reasons.append(f"DASHA.AGREES.{name}")

    # -- RKT-03 caution: Ketu transiting the 10th from lagna --------------------
    if axis["ketu_house_from_lagna"] == 10:
        cautions.append("KETU.TENTH")

    # -- band ------------------------------------------------------------------
    if score >= 4:
        band = "Favorable"
    elif score >= 1:
        band = "Mixed"
    else:
        band = "Challenging"

    # -- Tier-3 passage pattern -------------------------------------------------
    if band == "Favorable" and dasha_agrees:
        pattern = "A"
    elif band in ("Favorable", "Mixed") and not dasha_agrees:
        pattern = "B"
    else:
        pattern = "C"

    return Verdict(band=band, score=score, reasons=reasons, cautions=cautions,
                   lead_contact=lead, pattern=pattern)

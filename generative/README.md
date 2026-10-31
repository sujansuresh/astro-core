# Generative Libraries — CAREER pilot

---

## GLOSSARY — Rule ID prefixes used in this file

> Master table: `rule-engine/RULES.md` → GLOSSARY. Only the prefixes used in this file are listed below.

| Prefix | விரிவாக்கம் | எதைக் குறிக்கிறது? |
|---|---|---|
| ORB | Orb / Contact Window | கிரகத் தொடுதலின் டிகிரி மற்றும் கால அளவு |
| REPORT | Report Generation | அறிக்கை உருவாக்கும் விதிகள் |
| PROF | Natal Profile | ஜாதகரின் அடிப்படைப் பண்புகள் |

---

> **Machine-readable source of truth:** the `.json` banks beside this file
> (`phrases.json`, `profile.json`, `career.json`). The engine loads the JSON.
> This `.md` documents structure and keying convention for human authoring.

## Keying convention

| Prefix | Meaning |
|---|---|
| `FRAME.*` | Tier-2 sentence frames summoned by blueprints |
| `BRIDGE.*` | Tier-3 pre-authored connectors |
| `AXIS.*` / `TIMING.*` | Tier-1 shared phrases (phrases.json) |
| `PROF.*` | Profile frames (profile.json, PROF-01..03) |
| `ANSWER.<BAND>.<DOMAIN>` | Section-4 verdict headline per band × domain |
| `REASON.*` / `CAUTION.*` | Named reasons/cautions from verdict keys |
| `EVENT.<NODE>.<PLANET>` | Dated ORB-02 event line per contact |

## Authoring workflow (Phase 3)

1. Assistant drafts banks in English (DRAFT status in `_status`).
2. Machan corrects line by line — corrected version IS the library.
3. Hand-simulated sample report → Machan grades → fixes go into the bank,
   never into the engine.

# engine/planet_relations.py

from typing import Tuple

def get_planet_relationship(major: str, minor: str) -> Tuple[str, str]:
    """
    Returns: (Nature, Description)
    Nature: "Good", "Bad", "Neutral"
    Description: Text based explanation from Vedastro logic
    """

    relations = {
        "Sun": {
            "Moon": ("Good", "Winning favour from superiors, increase in business, fresh enterprises..."),
            "Mars": ("Bad", "Rheumatic troubles, quarrels, danger of fever, loss of money..."),
            "Mercury": ("Neutral", "Gain in money, good reputation, but nervous weakness and disputes...")
            # continue all 9
        },
        "Moon": {
            "Sun": ("Neutral", "Feverish complaints, legal power, success or failure..."),
            "Mars": ("Bad", "Quarrels, litigation, danger from fever, loss of blood..."),
            "Jupiter": ("Good", "Increase of property, birth of a child, honour...")
            # continue all 9
        },
        # ... Add all 9 planets as major with 9 minors each
    }

    # Fallback handling
    try:
        return relations[major][minor]
    except KeyError:
        return ("Unknown", "No relationship data available.")

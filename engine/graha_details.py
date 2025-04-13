 # graha_details.py
from engine.rasi_chart import SIGNS, to_dms_string

# Nakshatra data: (Name, Lord)
NAKSHATRAS = [
    ("Ashwini", "Ketu"), ("Bharani", "Venus"), ("Krittika", "Sun"),
    ("Rohini", "Moon"), ("Mrigashira", "Mars"), ("Ardra", "Rahu"),
    ("Punarvasu", "Jupiter"), ("Pushya", "Saturn"), ("Ashlesha", "Mercury"),
    ("Magha", "Ketu"), ("Purva Phalguni", "Venus"), ("Uttara Phalguni", "Sun"),
    ("Hasta", "Moon"), ("Chitra", "Mars"), ("Swati", "Rahu"),
    ("Vishakha", "Jupiter"), ("Anuradha", "Saturn"), ("Jyeshtha", "Mercury"),
    ("Mula", "Ketu"), ("Purva Ashadha", "Venus"), ("Uttara Ashadha", "Sun"),
    ("Shravana", "Moon"), ("Dhanishta", "Mars"), ("Shatabhisha", "Rahu"),
    ("Purva Bhadrapada", "Jupiter"), ("Uttara Bhadrapada", "Saturn"), ("Revati", "Mercury")
]

# Planetary dignity chart (Sign-based)
DIGNITY = {
    "Sun":     {"exalt": "Aries",     "debil": "Libra",     "own": ["Leo"]},
    "Moon":    {"exalt": "Taurus",    "debil": "Scorpio",   "own": ["Cancer"]},
    "Mars":    {"exalt": "Capricorn", "debil": "Cancer",    "own": ["Aries", "Scorpio"]},
    "Mercury": {"exalt": "Virgo",     "debil": "Pisces",    "own": ["Gemini", "Virgo"]},
    "Jupiter": {"exalt": "Cancer",    "debil": "Capricorn", "own": ["Sagittarius", "Pisces"]},
    "Venus":   {"exalt": "Pisces",    "debil": "Virgo",     "own": ["Taurus", "Libra"]},
    "Saturn":  {"exalt": "Libra",     "debil": "Aries",     "own": ["Capricorn", "Aquarius"]},
    "Rahu":    {"exalt": "Taurus",    "debil": "Scorpio",   "own": []},
    "Ketu":    {"exalt": "Scorpio",   "debil": "Taurus",    "own": []}
}

def get_nakshatra_info(true_long):
    """Given a nirayana longitude, return nakshatra name, pada, and lord."""
    total_nakshatra_deg = 13 + 1/3  # 13°20′ = 13.333...
    nak_index = int(true_long // total_nakshatra_deg)
    nak_name, nak_lord = NAKSHATRAS[nak_index]

    deg_within_nak = true_long % total_nakshatra_deg
    pada = int(deg_within_nak // (total_nakshatra_deg / 4)) + 1

    return nak_name, pada, nak_lord

def get_dignity(graha, sign):
    """Returns the dignity of a graha based on its sign."""
    if graha not in DIGNITY:
        return "-"
    
    if sign == DIGNITY[graha]["exalt"]:
        return "Exalted"
    elif sign == DIGNITY[graha]["debil"]:
        return "Debilitated"
    elif sign in DIGNITY[graha]["own"]:
        return "Own"
    else:
        return "Neutral"


def get_graha_detail_table(rasi_chart):
    """Returns tabular graha detail output based on input Rasi chart."""
    graha_table = []

    for graha, data in rasi_chart.items():
        sign = data["sign"]
        degree = data["degree"]
        dms = data["dms"]
        abs_long = SIGNS.index(sign) * 30 + degree

        nak, pada, lord = get_nakshatra_info(abs_long)

        dignity = get_dignity(graha, sign)

        graha_table.append({
            "Graha": graha,
            "Rasi": sign,
            "DMS": dms,
            "Nakshatra": f"{nak} - {pada}",
            "Nakshatra Lord": lord,
            "Dignity": dignity,
            "Retrograde": "Yes" if data["retrograde"] else "No"
        })


    return graha_table

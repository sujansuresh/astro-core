import swisseph as swe
from datetime import datetime

# Constants
PLANETS = [
    swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS,
    swe.JUPITER, swe.SATURN, swe.MEAN_NODE  # Rahu
]

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def to_dms_string(degree_float):
    deg = int(degree_float)
    rem = (degree_float - deg) * 60
    mins = int(rem)
    secs = int((rem - mins) * 60)
    return f"{deg:02d}° {mins:02d}′ {secs:02d}″"

def get_rasi_chart(jd, lat, lon):
    swe.set_sid_mode(swe.SIDM_LAHIRI)  # KP Ayanamsa
    swe.set_topo(lon, lat, 0)

    # Calculate Ayanamsa explicitly
    ayanamsa = swe.get_ayanamsa_ut(jd)

    chart = {}

    # Planets
    for planet in PLANETS:
        pos, _ = swe.calc_ut(jd, planet, swe.FLG_SWIEPH | swe.FLG_SPEED)
        true_lon = pos[0] - ayanamsa
        if true_lon < 0:
            true_lon += 360
        sign_index = int(true_lon // 30)
        sign = SIGNS[sign_index]
        degree = true_lon % 30
        retro = pos[3] < 0

        name = swe.get_planet_name(planet)
        if planet == swe.MEAN_NODE:
            name = "Rahu"

        chart[name] = {
            "sign": sign,
            "degree": round(degree, 2),
            "dms": to_dms_string(degree),
            "retrograde": retro
        }

    # Ketu (exactly opposite of Rahu)
    rahu_long = (chart["Rahu"]["degree"] + SIGNS.index(chart["Rahu"]["sign"]) * 30)
    ketu_long = (rahu_long + 180) % 360
    ketu_sign_index = int(ketu_long // 30)
    ketu_sign = SIGNS[ketu_sign_index]
    ketu_degree = ketu_long % 30

    chart["Ketu"] = {
        "sign": ketu_sign,
        "degree": round(ketu_degree, 2),
        "dms": to_dms_string(ketu_degree),
        "retrograde": True
    }

    # Ascendant (Lagna)
    cusps, _ = swe.houses(jd, lat, lon)
    asc_true = cusps[0] - ayanamsa
    if asc_true < 0:
        asc_true += 360
    asc_sign_index = int(asc_true // 30)
    asc_sign = SIGNS[asc_sign_index]
    asc_degree = asc_true % 30

    chart["Ascendant"] = {
        "sign": asc_sign,
        "degree": round(asc_degree, 2),
        "dms": to_dms_string(asc_degree),
        "retrograde": False
    }

    return chart

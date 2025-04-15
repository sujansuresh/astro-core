from datetime import datetime, timedelta
import swisseph as swe
#from engine.utils import to_dms_string

# Constants
WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
RASHIS = [
    "Mesha", "Vrishabha", "Mithuna", "Kataka", "Simha", "Kanya",
    "Tula", "Vrischika", "Dhanus", "Makara", "Kumbha", "Meena"
]
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
KARANAS = ["Bava", "Balava", "Kaulava", "Taitila", "Garija", "Vanija", "Vishti", "Shakuni", "Chatushpada", "Naga", "Kimstughna"]

TAMIL_MONTHS = [
    ("Chithirai", (4, 14)), ("Vaikasi", (5, 15)), ("Aani", (6, 15)), ("Aadi", (7, 16)),
    ("Avani", (8, 17)), ("Purattasi", (9, 17)), ("Aippasi", (10, 17)), ("Karthigai", (11, 16)),
    ("Margazhi", (12, 16)), ("Thai", (1, 14)), ("Maasi", (2, 13)), ("Panguni", (3, 14))
]

def get_tamil_month(day, month):
    for name, (m, start_day) in TAMIL_MONTHS:
        if month == m and day >= start_day:
            return name
        elif (month == (m + 1) % 12 or (m == 12 and month == 1)) and day < start_day:
            return name
    return "Unknown"

def get_panchang(date, lat=10.3833, lon=78.0833):
    swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)
    swe.set_topo(lon, lat, 0)

    jd = swe.julday(date.year, date.month, date.day, 5.5)  # approx sunrise time (5:30 AM IST)

    weekday = WEEKDAYS[date.weekday()]
    tamil_month = get_tamil_month(date.day, date.month)

    # Moon & Sun positions
    moon_pos = swe.calc_ut(jd, swe.MOON)[0][0]
    sun_pos = swe.calc_ut(jd, swe.SUN)[0][0]
    ayanamsa = swe.get_ayanamsa_ut(jd)
    moon_niry = (moon_pos - ayanamsa) % 360
    sun_niry = (sun_pos - ayanamsa) % 360

    # Rashi
    moon_sign = RASHIS[int(moon_niry // 30)]

    # Nakshatra
    nak_deg = 13.333333
    nak_index = int(moon_niry // nak_deg)
    nak_name, nak_lord = NAKSHATRAS[nak_index]
    pada = int((moon_niry % nak_deg) // (nak_deg / 4)) + 1

    # Tithi
    tithi_index = int(((moon_niry - sun_niry) % 360) / 12)
    paksha = "Shukla" if tithi_index < 15 else "Krishna"
    tithi = tithi_index + 1 if tithi_index < 15 else tithi_index - 14

    # Yoga
    yoga_index = int(((moon_niry + sun_niry) % 360) // (360 / 27))
    yoga_name = NAKSHATRAS[yoga_index][0]

    # Karana
    karana_index = int((((moon_niry - sun_niry) % 360) / 6)) % 11
    karana = KARANAS[karana_index]

    # Yogi / Avayogi
    yogi_lord = NAKSHATRAS[yoga_index][1]
    avayogi_lord = NAKSHATRAS[(yoga_index + 6) % 27][1]

    # Tithi Shunya simplified
    tithi_shunya = []
    if tithi in [5, 6, 7, 11]:
        tithi_shunya.append("Moon in Leo")
    if tithi in [8, 12, 13]:
        tithi_shunya.append("Moon in Virgo")
    if tithi in [1, 2]:
        tithi_shunya.append("Moon in Cancer")

    return {
        "Weekday": weekday,
        "Tamil Month": f"{tamil_month} - {date.day}",
        "Rashi": moon_sign,
        "Tithi": f"{tithi} ({paksha})",
        "Nakshatra": f"{nak_name}-{pada}",
        "Nakshatra Lord": nak_lord,
        "Yoga": yoga_name,
        "Karana": karana,
        "Yogi": yogi_lord,
        "Avayogi": avayogi_lord,
        "Tithi Shunya": ", ".join(tithi_shunya)
    }

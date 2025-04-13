from datetime import datetime, timedelta
import swisseph as swe
import pandas as pd

# Use Lahiri Ayanamsa for screenshot match
swe.set_sid_mode(swe.SIDM_KRISHNAMURTI)

DASA_ORDER = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
DASA_YEARS = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
    "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17
}
NAKSHATRA_SIZE = 13.333333  # Exact Vedic value (13°20') # 13.333...

def get_nirayana_moon_deg(jd_ut):
    pos, _ = swe.calc_ut(jd_ut, swe.MOON)
    ayanamsa = swe.get_ayanamsa_ut(jd_ut)
    return (pos[0] - ayanamsa) % 360

def get_nakshatra_index_and_remaining_deg(moon_long):
    nak_index = int(moon_long // NAKSHATRA_SIZE)
    degs_in_nakshatra = moon_long % NAKSHATRA_SIZE
    degs_remaining = NAKSHATRA_SIZE - degs_in_nakshatra
    return nak_index, degs_remaining, degs_in_nakshatra  # ✅ return 3 values

def get_dasa_lord(nak_index):
    return DASA_ORDER[nak_index % 9]

from dateutil.relativedelta import relativedelta

def format_period(start, end):
    delta = relativedelta(end, start)
    return f"{delta.years}Y {delta.months}M {delta.days}D"

from dateutil.relativedelta import relativedelta

def get_bhukti_timeline(start_date, dasa_lord, duration_years, dob):
    timeline = []
    start_index = DASA_ORDER.index(dasa_lord)
    ordered_bhuktis = DASA_ORDER[start_index:] + DASA_ORDER[:start_index]

    current = start_date
    for bhukti_lord in ordered_bhuktis:
        bhukti_years = (duration_years * DASA_YEARS[bhukti_lord]) / 120
        days = round(bhukti_years * 365.25)
        end = current + timedelta(days=days)

        # ✅ Period in Y M D
        diff = relativedelta(end, current)
        period_str = f"{diff.years}Y {diff.months}M {diff.days}D"

        # ✅ Age from DOB to current Bhukti start
        age = relativedelta(current, dob)
        age_str = f"{age.years}Y {age.months}M {age.days}D"

        timeline.append({
            "Dasa": dasa_lord,
            "Bhukti": bhukti_lord,
            "Start": current.strftime("%Y-%m-%d"),
            "End": end.strftime("%Y-%m-%d"),
            "Period": period_str,
            "Age": age_str
        })

        current = end

    return timeline


def get_dasa_bhukti_timeline(jd_ut, birth_datetime_ist):
    moon_long = get_nirayana_moon_deg(jd_ut)
    nak_index, degs_remaining, degs_in_nakshatra = get_nakshatra_index_and_remaining_deg(moon_long)

    start_dasa = get_dasa_lord(nak_index)
    total_dasa_years = DASA_YEARS[start_dasa]

    # 🧠 Womb Stay Correction (Garbhachcha Bala)
    pada = int(degs_in_nakshatra // (NAKSHATRA_SIZE / 4)) + 1
    padas_remaining = 4 - pada + 1
    deg_per_pada = NAKSHATRA_SIZE / 4
    degs_remaining_adjusted = padas_remaining * deg_per_pada

    balance_years = (degs_remaining_adjusted / 13.334) * total_dasa_years
    passed_years = total_dasa_years - balance_years

    dasa_start = birth_datetime_ist - timedelta(days=round(passed_years * 365.25))

    timeline = []
    index = DASA_ORDER.index(start_dasa)

    for i in range(9):
        dasa_lord = DASA_ORDER[(index + i) % 9]
        duration = DASA_YEARS[dasa_lord]
        if i == 0:
            duration = balance_years
        bhuktis = get_bhukti_timeline(dasa_start, dasa_lord, duration, birth_datetime_ist)
        timeline.extend(bhuktis)
        dasa_start += timedelta(days=round(duration * 365.25))

    return pd.DataFrame(timeline)

def generate_dasa_bhukti_timeline(dob_str, time_str, latitude, longitude, timezone_offset=5.5):
    dt = datetime.strptime(f"{dob_str} {time_str}", "%Y-%m-%d %H:%M")
    birth_datetime_utc = dt - timedelta(hours=timezone_offset)

    jd = swe.julday(
        birth_datetime_utc.year,
        birth_datetime_utc.month,
        birth_datetime_utc.day,
        birth_datetime_utc.hour + birth_datetime_utc.minute / 60
    )
    swe.set_topo(longitude, latitude, 0)
    return get_dasa_bhukti_timeline(jd, dt)
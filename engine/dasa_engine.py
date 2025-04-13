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
NAKSHATRA_SIZE = 13 + 1/3  # 13.333...

def get_nirayana_moon_deg(jd_ut):
    pos, _ = swe.calc_ut(jd_ut, swe.MOON)
    ayanamsa = swe.get_ayanamsa_ut(jd_ut)
    return (pos[0] - ayanamsa) % 360

def get_nakshatra_index_and_remaining_deg(moon_long):
    nak_index = int(moon_long // NAKSHATRA_SIZE)
    degs_in_nakshatra = moon_long % NAKSHATRA_SIZE
    degs_remaining = NAKSHATRA_SIZE - degs_in_nakshatra
    return nak_index, degs_remaining

def get_dasa_lord(nak_index):
    return DASA_ORDER[nak_index % 9]

def get_bhukti_timeline(start_date, dasa_lord, duration_years):
    timeline = []
    start_index = DASA_ORDER.index(dasa_lord)
    ordered_bhuktis = DASA_ORDER[start_index:] + DASA_ORDER[:start_index]

    current = start_date
    for bhukti_lord in ordered_bhuktis:
        bhukti_years = (duration_years * DASA_YEARS[bhukti_lord]) / 120
        end = current + timedelta(days=round(bhukti_years * 365.25))
        timeline.append({
            "Dasa": dasa_lord,
            "Bhukti": bhukti_lord,
            "Start": current.strftime("%Y-%m-%d")
        })
        current = end

    return timeline

def get_dasa_bhukti_timeline(jd_ut, birth_datetime_ist):
    moon_long = get_nirayana_moon_deg(jd_ut)
    nak_index, degs_remaining = get_nakshatra_index_and_remaining_deg(moon_long)

    start_dasa = get_dasa_lord(nak_index)
    total_dasa_years = DASA_YEARS[start_dasa]
    balance_years = (degs_remaining / 13.333) * total_dasa_years
    passed_years = total_dasa_years - balance_years

    dasa_start = birth_datetime_ist - timedelta(days=round(passed_years * 365.25))

    timeline = []
    index = DASA_ORDER.index(start_dasa)

    for i in range(9):
        dasa_lord = DASA_ORDER[(index + i) % 9]
        duration = DASA_YEARS[dasa_lord]
        if i == 0:
            duration = balance_years
        bhuktis = get_bhukti_timeline(dasa_start, dasa_lord, duration)
        timeline.extend(bhuktis)
        dasa_start += timedelta(days=round(duration * 365.25))

    return pd.DataFrame(timeline)

def generate_dasa_bhukti_timeline(jd_ut, dob_str, time_str, timezone_offset=5.5):
    dt = datetime.strptime(f"{dob_str} {time_str}", "%Y-%m-%d %H:%M")
    birth_datetime_utc = dt - timedelta(hours=timezone_offset)
    jd = swe.julday(birth_datetime_utc.year, birth_datetime_utc.month, birth_datetime_utc.day,
                    birth_datetime_utc.hour + birth_datetime_utc.minute / 60)
    return get_dasa_bhukti_timeline(jd, dt)

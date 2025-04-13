from datetime import datetime
from geopy.geocoders import Nominatim
import pytz
import swisseph as swe

def get_birth_data(date_str, time_str, place_str):
    full_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

    # Geocode the place
    geolocator = Nominatim(user_agent="astro-core")
    location = geolocator.geocode(place_str)

    if not location:
        raise Exception(f"Location '{place_str}' not found")

    lat = location.latitude
    lon = location.longitude

    # 👇 Fallback logic to find country code safely
    country_guess = "IN"  # Assume India for Dindigul
    try:
        raw_addr = location.raw.get("address", {})
        country_code = raw_addr.get("country_code", None)
        if country_code:
            country_guess = country_code.upper()
    except:
        pass

    # Timezone resolution
    try:
        timezone = pytz.timezone(pytz.country_timezones[country_guess][0])
    except Exception as e:
        raise Exception(f"Could not determine timezone for location '{place_str}'") from e

    local_dt = timezone.localize(full_datetime)
    utc_dt = local_dt.astimezone(pytz.utc)
    utc_offset = int((local_dt.utcoffset().total_seconds()) / 3600)

    # Julian Day calculation
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour + utc_dt.minute / 60.0)

    return {
        "input_date": date_str,
        "input_time": time_str,
        "input_place": place_str,
        "latitude": lat,
        "longitude": lon,
        "timezone": str(timezone),
        "utc": utc_dt.strftime("%Y-%m-%d %H:%M"),
        "utc_offset": utc_offset,
        "julian_day": jd
    }

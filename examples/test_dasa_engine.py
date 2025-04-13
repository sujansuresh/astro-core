from engine.dasa_engine import generate_dasa_bhukti_timeline

# Static test for Dindigul
birth_date = "1992-03-02"
birth_time = "22:17"  # IST
latitude = 10.3833
longitude = 77.75  # ← more accurate for Dindigul
timezone = 5.5

df = generate_dasa_bhukti_timeline(
    dob_str=birth_date,
    time_str=birth_time,
    latitude=latitude,
    longitude=longitude,
    timezone_offset=timezone
)

print(df.to_string(index=False))

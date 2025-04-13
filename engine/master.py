from engine.input_handler import get_birth_data
from engine.rasi_chart import get_rasi_chart
from engine.amsa_chart import get_navamsa_chart
from engine.graha_details import get_graha_details
from engine.dasa_engine import generate_dasa_bhukti_timeline

def print_full_chart(dob, tob, place):
    # Step 1: Get birth data
    data = get_birth_data(dob, tob, place)
    jd = data['julian_day']
    lat = data['latitude']
    lon = data['longitude']
    dob_dt = data['datetime_obj']

    # Step 2: Display Birth Details
    print("\n📌 Birth Details")
    print(f"Date of Birth : {dob}")
    print(f"Time of Birth : {tob}")
    print(f"Place         : {place}")
    print(f"Latitude      : {lat}")
    print(f"Longitude     : {lon}")

    # Step 3: Generate and Display Rasi Chart
    rasi = get_rasi_chart(jd, lat, lon)
    print("\n🪐 Rasi Chart")
    for planet, info in rasi.items():
        retro = " (R)" if info['retrograde'] else ""
        print(f"{planet:10}: {info['sign']:10} {info['dms']:>10} {retro}")

    # Step 4: Generate and Display Navamsa Chart
    navamsa = get_navamsa_chart(jd, lat, lon, rasi)
    print("\n🌟 Navamsa Chart (Thirukkanidham)")
    for planet, info in navamsa.items():
        print(f"{planet:10}: {info['navamsa_sign']:10} ← from {info['rasi_sign']:10} {info['dms']}")

    # Step 5: Generate and Display Graha Details
    graha_df = get_graha_details(jd, lat, lon)
    print("\n📋 Graha Details")
    for row in graha_df:
        print(f"{row['Graha']:10} | {row['Rasi']:10} | {row['DMS']:>10} | {row['Nakshatra']:20} | {row['Nakshatra Lord']:10} | {'R' if row['Retrograde'] == 'Yes' else '-'} | {row['Dignity']}")


    # Step 6: Generate and Display Dasa Bhukti Timeline
    dasa_df = generate_dasa_bhukti_timeline(dob, tob, lat, lon)
    print("\n📅 Vimshottari Dasa Timeline")
    print(dasa_df.to_string(index=False))

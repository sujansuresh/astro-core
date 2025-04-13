from engine.input_handler import get_birth_data
from engine.rasi_chart import get_rasi_chart
from engine.amsa_chart import get_navamsa_chart

# Step 1: Provide birth details
dob = "1992-03-02"
time = "22:05"
place = "Dindigul"

# Step 2: Get geolocation, JD and coords
data = get_birth_data(dob, time, place)
jd = data['julian_day']
lat = data['latitude']
lon = data['longitude']

# Step 3: Generate Rasi chart
rasi = get_rasi_chart(jd, lat, lon)

# Step 4: Generate Navamsa chart
navamsa = get_navamsa_chart(jd, lat, lon, rasi)

# Step 5: Display
print("\n🪐 Rasi Chart")
for planet, info in rasi.items():
    print(f"{planet:10}: {info['sign']:10} {info['dms']} {'(R)' if info['retrograde'] else ''}")

print("\n🧭 Navamsa Chart (Thirukkanidham)")
for planet, info in navamsa.items():
    print(f"{planet:10}: {info['navamsa_sign']:10} ← from {info['rasi_sign']} {info['dms']}")

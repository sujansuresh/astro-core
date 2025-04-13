from engine.input_handler import get_birth_data
from engine.rasi_chart import get_rasi_chart
from engine.amsa_chart import get_navamsa_chart

# Step 1: Get birth data and Julian day
data = get_birth_data("1992-03-02", "22:05", "Dindigul")

# Step 2: Generate the Rasi chart
rasi = get_rasi_chart(data['julian_day'], data['latitude'], data['longitude'])

# Step 3: Generate Navamsa chart from Rasi
navamsa = get_navamsa_chart(rasi)

# Step 4: Display output
print("\n--- Navamsa Chart ---")
for planet, info in navamsa.items():
    print(f"{planet}: {info['navamsa_sign']} (from {info['rasi_sign']} {info['degree']}°)")

from engine.rasi_chart import get_rasi_chart
from engine.amsa_chart import get_navamsa_chart
from engine.input_handler import get_birth_data

# Sample birth data
data = get_birth_data("1992-03-02", "22:05", "Dindigul")
rasi_chart = get_rasi_chart(data["julian_day"], data["latitude"], data["longitude"])
navamsa_chart = get_navamsa_chart(data["julian_day"], data["latitude"], data["longitude"], rasi_chart)

# Display Navamsa chart
print("\n--- Navamsa Chart ---")
for planet, info in navamsa_chart.items():
    print(f"{planet:<10}: {info['navamsa_sign']} ← {info['rasi_sign']} {info['degree']}°")

from datetime import datetime
from engine.panchang import get_panchang

# Birth details
date = datetime(1992, 3, 2)
lat = 10.3833
lon = 78.0833

panchang = get_panchang(date, lat, lon)

print("\n📅 Panchangam Details")
for key, val in panchang.items():
    print(f"{key:20}: {val}")

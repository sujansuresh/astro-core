from engine.input_handler import get_birth_data
from engine.rasi_chart import get_rasi_chart
from engine.graha_details import get_graha_detail_table
import pandas as pd

# Sujan's birth details
birth = get_birth_data("1992-03-02", "22:05", "Dindigul")

# Compute Rasi chart
rasi_chart = get_rasi_chart(birth["julian_day"], birth["latitude"], birth["longitude"])

# Fetch graha details from rasi
graha_table = get_graha_detail_table(rasi_chart)

# Display it like a pro
df = pd.DataFrame(graha_table)
print("\n--- Graha Details ---")
print(df)

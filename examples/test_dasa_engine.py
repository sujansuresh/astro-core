from engine.dasa_engine import generate_dasa_bhukti_timeline

birth_date = "1992-03-02"
birth_time = "22:17"  # IST
df = generate_dasa_bhukti_timeline(None, birth_date, birth_time)

print(df.to_string(index=False))

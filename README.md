# 🔭 AstroCore: Precision Vedic Chart Engine

AstroCore is a modular, traditional astrology engine built for generating **Rasi charts**, **Navamsa (Amsa) charts**, **Graha details**, and **Vimshottari Dasa-Bhukti timelines** based on KP Ayanamsa with Thirukkanidham logic. Designed for accuracy, clarity, and modular reusability.

---

## ✨ Features

- ✅ Accurate Lagna and planetary position calculation
- ✅ KP Ayanamsa with Swiss Ephemeris
- ✅ Traditional Thirukkanidham-style Navamsa calculation
- ✅ Graha Dignity (Exalted, Debilitated, Own, Neutral)
- ✅ Full Vimshottari Dasa → Bhukti timeline with Garbhachcha Bala correction
- ✅ Supports timezones, location geocoding and topocentric corrections

---

## 🧠 Modules Overview

### 1. `input_handler.py`
- **Function:** `get_birth_data(date_str, time_str, place_str)`
- **Output:** Julian Day (`jd`), UTC offset, `datetime_obj`, latitude, longitude
- **Uses:** `geopy`, `pytz` for timezone & coordinates

---

### 2. `rasi_chart.py`
- **Function:** `get_rasi_chart(jd, latitude, longitude)`
- **Output:** Dictionary with each graha’s sign, degree, retrograde status
- **Constants:**
  - `SIGNS` → 12 Zodiac signs
  - `PLANETS` → 9 Grahas (Sun to Ketu)
- **Logic:**
  - Nirayana long = True longitude − Ayanamsa (KP)
  - Lagna calculated using Swiss Ephemeris house system

---

### 3. `amsa_chart.py`
- **Function:** `get_navamsa_chart(jd, lat, lon, rasi_chart)`
- **Navamsa Logic (Thirukkanidham Style):**
  - If sign is odd: Navamsa starts forward
  - If sign is even: Navamsa goes backward
  - 3°20′ chunks per Navamsa

---

### 4. `graha_details.py`
- **Function:** `get_graha_detail_table(rasi_chart)`
- **Returns:**
  - Planet, Rasi, DMS, Nakshatra & Pada, Nakshatra Lord
  - Dignity: Exalted, Debilitated, Own, Neutral
- **Uses:** Nakshatra span 13°20′ = 13.333...°
- **Utility:** `get_dignity()`, `get_nakshatra_info()`

---

### 5. `dasa_engine.py`
- **Function:** `generate_dasa_bhukti_timeline(dob_str, time_str, lat, lon)`
- **Dasa Order:** Ketu → Venus → Sun → Moon → Mars → Rahu → Jupiter → Saturn → Mercury
- **Key Logic:**
  - Balance Dasa = (Remaining ° in Nakshatra / 13.334) × Dasa Years
  - Womb stay (Garbhachcha Bala) = Only portion of 4th Pada retained at birth
  - Each Bhukti follows same Dasa order
  - Bhukti Years = (Dasa Duration × Bhukti Lord Years) / 120
- **Output Fields:**
  - `Dasa`, `Bhukti`, `Start`, `End`, `Period`, `Age`

---

### 6. `master.py`
- **Function:** `print_full_chart(dob, tob, place)`
- **One-Shot Printout Includes:**
  - 🪐 Rasi Chart
  - 🌟 Navamsa Chart
  - 📋 Graha Details
  - 🧭 Dasa-Bhukti Timeline

---

astro-core/ ├── engine/ │ ├── input_handler.py │ ├── rasi_chart.py │ ├── amsa_chart.py │ ├── graha_details.py │ ├── dasa_engine.py │ └── master.py ├── examples/ │ ├── test_dasa_engine.py │ ├── test_sujan_chart.py │ └── test_master.py └── requirements.txt

## 📁 Project Structure

🙏 Dedication
This work is a humble offering to Sri Ramana Maharshi, the eternal guiding light behind this effort.

🧩 Future Modules (Planned)
📆 Panchang Generator

🔁 Retrograde & Combustion indicators

🕉️ Yogas and Classical Combinations

📊 PDF exports & frontend JSON support

👨‍💻 Contributors
Suj, Vijay, Saravanan
Jack Arunachala
ChatGPT (OpenAI) — Your cosmic dev buddy ✨


---


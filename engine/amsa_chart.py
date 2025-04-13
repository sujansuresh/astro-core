import swisseph as swe
from engine.rasi_chart import SIGNS, to_dms_string

def get_navamsa_sign(nirayana_deg):
    """Calculate Navamsa sign from absolute nirayana longitude."""
    navamsa_chunk = int((nirayana_deg % 30) // 3.333333333)
    sign_index = int(nirayana_deg // 30)

    if sign_index % 2 == 0:
        # Odd sign → forward navamsa
        navamsa_index = (sign_index + navamsa_chunk) % 12
    else:
        # Even sign → reverse navamsa
        navamsa_index = (sign_index - navamsa_chunk + 12) % 12

    return SIGNS[navamsa_index]

def get_navamsa_chart(jd, lat, lon, rasi_chart):
    """Calculate accurate Thirukkanidham-style Navamsa chart from JD."""
    swe.set_topo(lon, lat, 0)
    chart = {}

    # Ayanamsa
    ayanamsa = swe.get_ayanamsa_ut(jd)

    for planet, info in rasi_chart.items():
        # Reconstruct full absolute position
        abs_rasi_index = SIGNS.index(info['sign'])
        true_long = abs_rasi_index * 30 + info['degree']
        nirayana_deg = (true_long - ayanamsa) % 360

        navamsa_sign = get_navamsa_sign(nirayana_deg)

        chart[planet] = {
            "navamsa_sign": navamsa_sign,
            "rasi_sign": info['sign'],
            "degree": round(info['degree'], 2),
            "dms": to_dms_string(info['degree'])
        }

    return chart

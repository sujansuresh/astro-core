def to_dms_string(decimal_degrees):
    deg = int(decimal_degrees)
    minutes_full = (decimal_degrees - deg) * 60
    min_ = int(minutes_full)
    sec = round((minutes_full - min_) * 60, 2)
    return f"{deg}°{min_}′{sec}″"

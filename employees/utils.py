from datetime import datetime
import pytz

def convert_to_timezone(dt, tz_name):
    local_tz = pytz.timezone(tz_name)
    return dt.astimezone(local_tz)

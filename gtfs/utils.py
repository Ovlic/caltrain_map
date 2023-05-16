
from datetime import datetime
from pytz import timezone

def toDateTime(str_time):
    str_time = str_time.replace("T", "-").replace("Z", "")
    date = datetime.strptime(str_time, "%Y-%m-%d-%H:%M:%S").replace(tzinfo=timezone('UTC'))
    date = date.astimezone(timezone('US/Pacific'))
    return date
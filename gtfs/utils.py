"""
This module contains utility functions for the GTFS package.
"""

from datetime import datetime
from pytz import timezone

def toDateTime(str_time) -> datetime:
    """Converts a string time to a datetime object.
    # Parameters:
    str_time: :class:`str`
        The string time to convert.
    """
    str_time = str_time.replace("T", "-").replace("Z", "")
    date = datetime.strptime(str_time, "%Y-%m-%d-%H:%M:%S").replace(tzinfo=timezone('UTC'))
    date = date.astimezone(timezone('US/Pacific'))
    return date
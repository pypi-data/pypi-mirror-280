import datetime
from time import time


def current_time():
    """get the current time

    Returns:
        str: time string
    """
    timestamp = datetime.datetime.fromtimestamp(time())
    str_time = timestamp.strftime("%Y%m%d%H%M%S")
    return str_time

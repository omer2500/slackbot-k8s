def calculate_pod_up_time(started_at, now):
    # returns a timedelta object
    diff = now - started_at
    res = "0m"

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (diff.days*1440 + diff.seconds/60)

    if hours> 24:
        res = f"{days}d"
    if hours > 1 and hours <=24:
        res = f"{hours}h"
    if minutes > 1 and minutes < 60:
        res = f"{int(minutes)}m"
    if seconds > 1 and seconds < 60:
        res = f"{int(seconds)}"

    return res
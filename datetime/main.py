from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

tz_utc_8 = timezone(timedelta(hours=0))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


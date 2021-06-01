

import datetime
import pytz

for tz in pytz.all_timezones:
    print(tz)

dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

td_mtn=dt_utcnow.astimezone(pytz.timezone('Indian/Reunion'))
print(td_mtn)
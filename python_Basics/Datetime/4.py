

import datetime
import pytz

dt= datetime.datetime(2021,5,31,7,30,29,tzinfo=pytz.UTC)
print(dt)

dtnow=datetime.datetime.now(tz=pytz.UTC)
print(dtnow)
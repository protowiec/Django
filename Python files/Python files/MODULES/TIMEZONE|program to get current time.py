#1 time of a timezone
from datetime import *
import pytz

tz_POLAND = pytz.timezone("Europe/Warsaw")
datetime_POLAND = datetime.now(tz_POLAND)
print("POLAND time: ", datetime_POLAND.strftime("%H:%M:%S"))

#2 current time
from datetime import datetime

now_method = datetime.now()
currentTime = now_method.strftime("%H:%M:%S")
print("Current time =", currentTime)

#3
from datetime import datetime

time = datetime.now().time()
print("Current Time =", time)

#4 using Time module
import time

Time = time.localtime()
currentTime = time.strftime("%H:%M:%S", Time)
print(currentTime)
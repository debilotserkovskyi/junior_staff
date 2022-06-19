import datetime
from datetime import time

timeIn = '12:30'
duration = 47
for position in range(0, len(timeIn)):
    if timeIn[position] == ':':
        hours = int(timeIn[0:position])
        minutes = int(timeIn[position+1:len(timeIn)])
        minutes = minutes + duration
        if minutes >= 60:
            hours += minutes//60
            minutes = minutes % 60
        if hours >= 24:
            hours = hours % 24
        print(time(hour=hours, minute=minutes).isoformat(timespec='minutes'))
        
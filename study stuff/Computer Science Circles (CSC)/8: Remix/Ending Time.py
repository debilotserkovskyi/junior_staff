import datetime
from datetime import time

timeIn = '08:30'
duration = 185
for position in range(0, len(timeIn)):
    if timeIn[position] == ':':
        hours = int(timeIn[0:position])
        minutes = int(timeIn[position+1:len(timeIn)])
        minutes = minutes + duration
        if minutes >= 60:
            minutes = minutes % 60
            hours += 1
        if hours >= 24:
            hours = hours % 24
        if duration >= 60:
            hours = (duration // 60) + hours
        elif (minutes + duration) % 60 > 0 and hours % 24 == hours and duration < 60:
            finalhr = hours + 1
        print(time(hour=hours, minute=minutes).isoformat(timespec='minutes'))
        
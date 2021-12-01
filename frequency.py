from datetime import datetime
import rplogging as logging



# hourly code, commences at the top of the hour
def hourly():
    now = datetime.now()
    if now.minute < 15:
        return True
    else:
        return False


# daily code, commences at the top of the hour at 4 AM
def daily():
    now = datetime.now()
    if now.hour == 4 and now.minute < 15:
        return True
    else:
        return False


# weekly code, commences on Monday at 4 AM
def weekly():
    now = datetime.now()
    if now.weekday == 0 and now.hour == 4 and now.minute < 15:
        return True
    else:
        return True


# commences hourly from 8 AM to 5 PM
def workday():
    now = datetime.now()
    if now.weekday < 5 and now.hour > 7 and now.hour < 17:
        return True
    else:
        return False

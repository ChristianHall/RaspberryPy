import rplogging as logging
from frequency import *

logging.info("starting RaspberryPy")

def test_frequency():
    if hourly():
        logging.info("HOURLY LOGGING SUCCESS")
    if daily():
        logging.info("DAILY LOGGING SUCCESS")
    if weekly():
        logging.info("WEEKLY LOGGING SUCCESS")
    if workday():
        logging.info("WORKDAY LOGGING SUCCESS")


test_frequency()

logging.info("finishing RaspberryPy")


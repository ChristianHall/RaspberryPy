import logging
from datetime import datetime
from constants import RASPY_INF, RASPY_ERR, RASPY_DBG


def write_log(message, file):
    if file != RASPY_DBG:
        with open(file, "a") as file:
            file.write(message)
    with open(RASPY_DBG, "a") as file:
        file.write(message)


def timestamp():
    now = datetime.now().strftime("%Y/%m/%D %H:%M:%S")
    return now


def info(message):
    now = timestamp()
    message = f"\n[ INF ] {now}\n{message}\n"
    write_log(message, RASPY_INF)


def warning(message):
    now = timestamp()
    message = f"\n[ WAR ] {now}\n{message}\n"
    write_log(message, RASPY_INF)


def error(message):
    now = timestamp()
    message = f"\n[ ERR ] {now}\n{message}\n"
    write_log(message, RASPY_ERR)


def critical(message):
    now = timestamp()
    message = f"\n[ !!! ] {now}\n{message}\n"
    write_log(message, RASPY_ERR)


def debug(message):
    now = timestamp()
    message = f"\n[ DBG ] {now}\n{message}\n"
    write_log(message, RASPY_DBG)


# def cleanlogs():
# clean log files if they are getting too large


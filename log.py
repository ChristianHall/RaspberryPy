# this handles all logging for all python applications
import os
from datetime import datetime
from constants import LOGGING_ERR, LOGGING_INFO, LOGGING_DBUG

def get_timestamp():
    return datetime.now().strftime("%m/%d/%Y %H:%M:%S")


def print_log(filepath, message):
    try:
        file = open(filepath, "a")
        file.write(message)
    except:
        pass
    finally:
        file.close()


def info(message):
    now = get_timestamp()
    print_log(LOGGING_INFO, f"\n{now}\n{message}\n")


def warning(message):
    now = get_timestamp()
    print_log(LOGGING_ERR, f"\nwarning    {now}\n{message}\n")


def error(message):
    now = get_timestamp()
    print_log(LOGGING_ERR, f"\nERROR      {now}\n{message}\n")


def critical(message):
    now = get_timestamp()
    print_log(LOGGING_ERR, f"\n[CRITICAL] {now}\n{message}\n")


def debug(message):
    now = get_timestamp()
    print_log(LOGGING_DBUG, f"\n{now}\n{message}\n")

# all constant variables are kept here
import os

# PROGRAM FILEPATH VARIABLES
DIRECTORY  = os.getcwd()
CONSTANTS  = DIRECTORY + "/constants.py"
FIREWRITER = DIRECTORY + "/filewriter.py"
LOGGING    = DIRECTORY + "/logging.py"
RASPBERRY  = DIRECTORY + "/raspberry.py"
SQLACCESS  = DIRECTORY + "/sqlaccess.py"
WRITEEMAIL = DIRECTORY + "/writeemail.py"

# OUTPUT FILE VARIABLES
LOGGING_INFO = DIRECTORY + "/raspberry.log"
LOGGING_ERR  = DIRECTORY + "/raspberry.err"
LOGGING_DBUG = DIRECTORY + "/raspberry.bug"
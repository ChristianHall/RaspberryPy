# all constant variables are kept here
import os


# WORKING DIRECTORY
DIRECTORY = os.getcwd()


# CORE FILES
RASPBERRY = DIRECTORY + "/raspberry.py"  # the script used to kick off all other scripts
CONSTANTS = DIRECTORY + "/constants.py"  # stores constants 
FREQUENCY = DIRECTORY + "/frequency.py"  # regulates time and frequency of functions
FILEWRITE = DIRECTORY + "/filewrite.py"  # creates, deletes, copies, examines, and moves files
GGLSHEETS = DIRECTORY + "/gglsheets.py"  # used for accessing information on google sheets
CONSOLEPY = DIRECTORY + "/consolepy.py"  # a password-protected GUI for settings
RPLOGGING = DIRECTORY + "/rplogging.py"  # used for all core logging
SENDEMAIL = DIRECTORY + "/sendemail.py"  # used sending emails
UPDATERPY = DIRECTORY + "/updaterpy.py"  # if a USB drive is found, updates all files with it
WEBACCESS = DIRECTORY + "/webaccess.py"  # used for web access functions 


# EXTERNAL FILES
EMLDOODLE = DIRECTORY + "/emldoodle.py"  # emails an encouraging email 8-5 M-F
DOODLEDAT = DIRECTORY + "/emldoodle.dat" # data file for emldoodle


# INPUT FILE DIRECTORIES
START_KEY = DIRECTORY + "/raspberry.key" # an indicator file that determines if program is on or off


# OUTPUT FILE DIRECTORIES
RASPY_INF = DIRECTORY + "/raspberry.log" # logs infos and warnings
RASPY_ERR = DIRECTORY + "/raspberry.err" # logs errors and criticals
RASPY_DBG = DIRECTORY + "/raspberry.dbg" # logs debugs
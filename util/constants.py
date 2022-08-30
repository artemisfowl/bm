"""
	@file constants.py
	@brief Util module component containing the constants to be used for this
	program
	@author sb
	@date Fri, 26 Aug 2022 00:15:24 +0530
	@bug No known bugs
"""

# Python version related
PY_VER_MAJOR = 3
PY_VER_MINOR = 8

# Configuration filepath default location
CONFIG_FILE_PATH = "./config/batterymonitor/config.ini"

# Configuration file contents
NOTIFICATION_SECTION = "notification"
MIN_BAT_PERCENT_OPTION = "minimum-battery-percent"
POLLING_FREQ = "polling-frequency"
NOTIFY_DURATION = "notification-duration"

DEFAULT_MIN_BAT_PERCENT = 30		# 30% battery capacity
DEFAULT_POLLING_FREQ = 10			# check every 10 seconds
DEFAULT_NOTIFY_DURATION = 5			# show the notification for 5 seconds

#!/usr/bin/env python

"""
	@file bm.py
	@brief Program to monitor the battery and alert user if the battery charge
	goes below the desired percentage
	@author sb
	@date Thu, 25 Aug 2022 23:55:36 +0530
	@bug No known bugs
"""

# standard libs/imports

# custom libs/modules
from util.commons import chk_pyver, panic, parse_cli_args, info, warn, parse_config_file
from util.constants import NOTIFICATION_SECTION, MIN_BAT_PERCENT_OPTION, POLLING_FREQ, NOTIFY_DURATION
from notifier.batterynotifier import BatteryNotifier

def main() -> int:
	"""
		@function main
		@brief Main function from where the function execution starts
		@return Returns 0 for success or -1 for failure
	"""
	errno = chk_pyver()
	if errno:
		return panic(errno=errno)

	parse_cli_args()
	info("Starting BatteryNotifier version 1")

	warn(msg="Debugging is enabled")
	info("Parse the configuration file")
	confdata = parse_config_file()
	warn(f"Minimum battery percent check : {int(confdata.get(NOTIFICATION_SECTION, MIN_BAT_PERCENT_OPTION))}")
	warn(f"Polling frequency : {int(confdata.get(NOTIFICATION_SECTION, POLLING_FREQ))}")
	warn(f"Notification message duration : {int(confdata.get(NOTIFICATION_SECTION, NOTIFY_DURATION))}")
	with BatteryNotifier() as batterynotifier:
		info("Calling notify")
		batterynotifier.notify(
				chk_battery_percent=int(confdata.get(NOTIFICATION_SECTION, MIN_BAT_PERCENT_OPTION)),
				polling_frequency=float(confdata.get(NOTIFICATION_SECTION, POLLING_FREQ)),
				toast_duration=int(confdata.get(NOTIFICATION_SECTION, NOTIFY_DURATION)))

	return 0

if __name__ == "__main__":
	main()

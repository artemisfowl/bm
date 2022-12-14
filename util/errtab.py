"""
	@file errtab.py
	@brief Util component containing the error string mappings
	@author sb
	@date Fri, 26 Aug 2022 00:23:48 +0530
	@bug No known bugs
"""

errtab = {
		-10: "Python version mismatch",
		# Battery notifier - error numbers
		-100: "Unable to set toast master, check platform specific imports",
		-1001: "Notification message data not provided",
		-1002: "Notification icon not provided",
		-1003: "Notification display duration value not correct"
}

"""
	@file batterynotifier.py
	@brief Notifier module component containing code for handling the battery monitoring task
	@author sb
	@date Sat, 27 Aug 2022 20:41:06 +0530
	@bug No known bugs
"""

class BatteryNotifier:
	"""
		@class BatteryNotifier
		@brief Class containing the functions for getting the system battery information
		@note This class will be a context manager - so the usage will contain 'with' statement
	"""
	def __init__(self) -> None:
		# battery related
		self._plugged_status = None
		self._battery = None

		# notification related
		self._notify_once = False
		self._toast_master = None

	def __enter__(self):
		return self

	#fixme: need to specify the type of the variables
	def __exit__(self, exc_type, exc_val, exc_tb):
		# check the type and then update the information of the parameters in the function signature
		print(type(exc_type))
		print(type(exc_val))
		print(type(exc_tb))
		pass

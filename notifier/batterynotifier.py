"""
	@file batterynotifier.py
	@brief Notifier module component containing code for handling the battery monitoring task
	@author sb
	@date Sat, 27 Aug 2022 20:41:06 +0530
	@bug No known bugs
"""

# custom libs/modules
from util.commons import info, warn, error

class BatteryNotifier:
	"""
		@class BatteryNotifier
		@brief Class containing the functions for getting the system battery information
		@note This class will be a context manager - so the usage will contain 'with' statement
	"""
	def __init__(self) -> None:
		"""
			@function __init__
			@brief Default constructor for BatteryNotifier class, sets value of member variables
			@return None
		"""
		# battery related
		self._plugged_status = None
		self._battery = None

		# notification related
		self._notify_once = False
		self._toast_master = None

	#fixme: Remove linter warning on providing the value of BatteryNotifier
	def __enter__(self):
		"""
			@function __enter__
			@brief Function to be executed when context manager is initialized
			@return Returns a reference to the current object of BatteryNotifier
		"""
		info("Starting context manager")
		warn("Returning a reference to self")
		return self

	#fixme: need to specify the type of the parameters
	def __exit__(self, exc_type, exc_val, exc_tb):
		info("Exiting context manager")
		# check the type and then update the information of the parameters in the function signature
		error(f"Exception type details : {type(exc_type)}")
		error(f"Exception value : {type(exc_val)}")
		error(f"Exception traceback : {type(exc_tb)}")

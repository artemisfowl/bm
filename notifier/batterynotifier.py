"""
	@file batterynotifier.py
	@brief Notifier module component containing code for handling the battery monitoring task
	@author sb
	@date Sat, 27 Aug 2022 20:41:06 +0530
	@bug No known bugs
"""

# standard libs/imports
from platform import system
from typing import Union
from time import sleep

# custom libs/modules
from util.commons import info, warn, error, panic

# third-party libs/imports
from psutil import sensors_battery
if system().lower() == "windows":					#fixme: pylint may report the following import
	from win10toast import ToastNotifier # pyright: reportMissingImports=false
elif system().lower() == "linux":
	from gi import require_version

	require_version("Notify", "0.7")
	from gi.repository import Notify, GdkPixbuf		#fixme: pylint may report, not sure why
	Notify.init("BM")

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
	def __exit__(self, exc_type, exc_val, exc_tb) -> None:

		"""
			@function __exit__
			@brief Function to be executed when the context manager is exiting
			@return None
		"""

		info("Exiting context manager")
		# check the type and then update the information of the parameters in the function signature
		error(f"Exception details : {exc_type}")
		error(f"Exception value : {exc_val}")
		error(f"Exception traceback : {exc_tb}")

	def _setup_notifier(self) -> int:

		"""
			@function setup_notifier
			@brief Function to setup the toasting/notifying handler
			@return Returns 0 if toast master has been set properly else sends -1xx series of error numbers
		"""

		info("Setting up the toast master")

		if system() == "Windows":
			info("Setting toastmaster for Windows OS")
			self._toast_master = ToastNotifier()
			warn("Toastmaster for windows has been set")
		elif system() == "Linux":
			info("Setting toastmaster for Linux")
			self._toast_master = Notify.Notification.new("BM")
			warn("Toastmaster for linux has been set")

		if self._toast_master is None:
			return -100

		return 0

	def _show_msg(self, msg: str, icon: str, duration: int) -> int:

		"""
			@function _show_msg
			@brief Function to show the battery status message as a notification
			@return Returns 0 on success, -1xxx series of error number on failure
		"""

		if msg is None or len(msg) == 0:
			return -1001

		if icon is None or len(icon) == 0:
			return -1002

		if duration is None or not isinstance(duration, int):
			return -1003

		# check the system and then setup the message information
		if system().lower() == "windows":
			info("Setting up notification for Windows platform")
			self._toast_master.show_toast(self._plugged_status, msg,
					icon_path=icon, duration=duration, threaded=True) # thread should always be set for Windows
		elif system().lower() == "linux":
			info("Setting up notification for Linux platform")
			self._toast_master.set_image_from_pixbuf(GdkPixbuf.Pixbuf.new_from_file(icon))
			self._toast_master.update(self._plugged_status, msg)
			self._toast_master.show()

		return 0

	def notify(self,
			chk_battery_percent:int, polling_frequency: float, toast_duration: int) -> Union[None, int]:

		"""
			@function notify
			@brief Function to notify the user about the status of the system battery
			@return Returns an error code based on the issue that is faced while notifying. 0 on success
		"""

		info("Notify service is starting")

		errno = self._setup_notifier()
		if errno:
			return panic(errno=errno)
		self._battery = sensors_battery()
		self._notify_once = not self._battery.power_plugged

		while True:
			#fixme: add the code for showing the notification
			self._battery = sensors_battery()
			self._plugged_status = "Plugged In" if self._battery.power_plugged else "Discharging"

			if self._battery.power_plugged:
				if not self._notify_once:
					self._show_msg(msg=f"Battery : {self._battery.percent}%",
							icon="./icons/charging_battery.ico",
							duration=toast_duration)
					self._notify_once = True
			else:
				if self._notify_once:
					self._show_msg(msg=f"Battery : {self._battery.percent}%",
							icon="./icons/discharging_battery.ico",
							duration=toast_duration)
					self._notify_once = False
				else:
					if self._battery.percent <= chk_battery_percent:
						self._show_msg(msg=f"Battery : {self._battery.percent}%",
								icon="./icons/30_battery.ico", duration=toast_duration)
			sleep(polling_frequency)

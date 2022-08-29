"""
	@file batterynotifier.py
	@brief Notifier module component containing code for handling the battery monitoring task
	@author sb
	@date Sat, 27 Aug 2022 20:41:06 +0530
	@bug No known bugs
"""

# standard libs/imports
from platform import system

# custom libs/modules
from util.commons import info, warn, error

# third-party libs/imports
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
	def __exit__(self, exc_type, exc_val, exc_tb):
		info("Exiting context manager")
		# check the type and then update the information of the parameters in the function signature
		error(f"Exception type details : {type(exc_type)}")
		error(f"Exception value : {type(exc_val)}")
		error(f"Exception traceback : {type(exc_tb)}")

	def _setup_notifier(self):
		"""
			@function setup_notifier
			@brief Function to setup the toasting/notifying handler
			@return None
		"""
		if system() == "Windows":
			info("Setting toastmaster for Windows OS")
			self._toast_master = ToastNotifier()
			warn("Toastmaster for windows has been set")
		elif system() == "Linux":
			info("Setting toastmaster for Linux")
			self._toast_master = Notify.Notification.new("BM")
			warn("Toastmaster for linux has been set")

	def notify(self) -> int:
		"""
			@function notify
			@brief Function to notify the user about the status of the system battery
			@return Returns an error code based on the issue that is faced while notifying. 0 on success
		"""
		info("Notify service is starting")
		self._setup_notifier()
		return 0

"""
	@file commons.py
	@brief Util module component containing the common utility functions
	@author sb
	@date Thu, 25 Aug 2022 23:59:45 +0530
	@bug No known bugs
"""

# standard libs/modules
from sys import version_info
from argparse import ArgumentParser
from datetime import datetime
from enum import Enum

# custom libs/modules
from .constants import PY_VER_MAJOR, PY_VER_MINOR, CONFIG_FILE_PATH
from .errtab import errtab
from .exceptions import UnknownErrorNumberError

# classes
class MessageType(Enum):
	"""
		@class MessageType
		@brief Enumeration class containing the symbols for Message types
	"""
	INFO = "\u24BE"
	DEBUG = "\u24cc"
	ERR = "\u24ba"

class Flags:
	"""
		@class Flags
		@brief Class containing the flags and values to be used by the program
	"""
	def __init__(self):
		self._isdebugenabled = False		# debugging enabled/disabled
		self._logfpath = None				# log filepath
		self._confpath = CONFIG_FILE_PATH	# configuration file path

	def set(self, isdebugenabled: bool, logfpath: str):
		"""
			@function set
			@brief Function to set the flags and configurations
			@return None
		"""
		self._isdebugenabled = isdebugenabled
		self._logfpath = logfpath

	def getdbgstatus(self) -> bool:
		"""
			@function getdbgstatus
			@brief Function to get the status of the debug enabled flag
			@return Returns True if debug enabled, else False
		"""
		return self._isdebugenabled

	def getlogfpath(self):
		"""
			@function getlogfpath
			@brief Function to get the log filepath set
			@return None
		"""
		return self._logfpath

flags = Flags()

def chk_pyver() -> int:
	"""
		@function chk_pyver
		@brief Function to check the Python version being used
		@return Returns 0 if version matches else returns -10
	"""
	if version_info.major >= PY_VER_MAJOR:
		if version_info.minor >= PY_VER_MINOR:
			return 0

	# remember that -10 is for Python version mismatch, refer to errtab
	return -10

def panic(errno: int):
	"""
		@function panic
		@brief Function to check the value of errno from the errtab and raise
		an exception accordingly
		@return None
	"""

	errkeys = [key for key, _ in errtab.items()]
	if errno not in set(errkeys):
		raise UnknownErrorNumberError(message="Unknown Error Number",
				errors=[])

	# if the error number is found, print the message set up
	print(errtab.get(errno))

def parse_cli_args():
	"""
		@function parse_cli_args
		@brief Function to parse the CLI arguments and set up the flags
		@return Returns True if debug enabled else returns False
	"""
	# will only be setting up the debug flag as of now
	_argparser = ArgumentParser()
	_argparser.add_argument("--debug", "-d",
			help="Enable debug logs", action="store_true")
	_argparser.add_argument("--log", "-l",
			help="Specify output log filepath", type=str)
	_argparser.add_argument("--config", "-c",
			help="Specify the configuration file path", type=str)

	_args = _argparser.parse_args()
	flags.set(
			isdebugenabled=vars(_args).get("debug"),	# type: ignore
			logfpath=vars(_args).get("log"))			# type: ignore

def parse_config_file():
	"""
		@function parse_config_file
		@brief Function to parse the configuration file and set up the values
	"""
	# first check if the configuration file along with the entire path is
	# present or not
	pass

def log(msg: str, msg_type: str):
	"""
		@function log
		@brief Function to log the provided message to the log file
		@return None
	"""
	if msg_type is None:
		return		# return the control to the calling routine

	# default to INFO if the type has not been provided
	msg_type = MessageType.INFO.value if msg_type is None else msg_type

	if flags.getdbgstatus():
		print(f"{datetime.now()} :: {msg_type} : {msg}")

		if flags.getlogfpath() is not None:
			with open(flags.getlogfpath(), "a", encoding="utf-8") as lfile: # type: ignore
				# append the newline since this is writing to the file
				lfile.write(f"{datetime.now()} :: {msg_type} : {msg}\n")

# alias functions
def info(msg: str):
	log(msg=msg, msg_type=MessageType.INFO.value)

def debug(msg: str):
	log(msg=msg, msg_type=MessageType.DEBUG.value)

def error(msg: str):
	log(msg=msg, msg_type=MessageType.ERR.value)

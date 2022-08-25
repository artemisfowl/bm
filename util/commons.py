"""
	@file commons.py
	@brief Util module component containing the common utility functions
	@author sb
	@date Thu, 25 Aug 2022 23:59:45 +0530
	@bug No known bugs
"""

# standard libs/modules
from sys import version_info

# custom libs/modules
from .constants import PY_VER_MAJOR, PY_VER_MINOR
from .errtab import errtab
from .exceptions import UnknownErrorNumberError

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

	if errno not in set(errtab.keys()):
		raise UnknownErrorNumberError(message="Unknown Error Number",
				errors=[])

	# if the error number is found, print the message set up
	print(errtab.get(errno))

def parse_cli_args():
	"""
		@function parse_cli_args
		@brief Function to parse the CLI arguments and set up the flags
		@return None
	"""
	return

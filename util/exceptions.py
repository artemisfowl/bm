"""
	@file exceptions.py
	@brief Util module component housing all the Exceptions
	@author sb
	@date Fri, 26 Aug 2022 00:34:10 +0530
	@bug No known bugs
"""

# create a generic Exception to be raised when Error number is not present in
# the error table
class UnknownErrorNumberError(Exception):
	"""
		@class UnknownErrorNumberError
		@brief Error to be raised when the Error number is not known
	"""
	def __init__(self, message, errors) -> None:
		super().__init__(message)
		self.errors = errors

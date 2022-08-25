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
from util.commons import chk_pyver, panic
from util.errtab import errtab

def main() -> int:
	"""
		@function main
		@brief Main function from where the function execution starts
		@return Returns 0 for success or -1 for failure
	"""
	errno = chk_pyver()
	if errno:
		panic(errno=errno)

	# now parse the CLI arguments
	return 0

if __name__ == "__main__":
	main()

#!/usr/bin/python3
"""" that prints the list, but sorted (ascending sort) """

class MyList(list):
	""" prints sprted list in asc order"""

	def print_sorted(self):
		""" print a sorted list in asc order """
		print(sorted(self))



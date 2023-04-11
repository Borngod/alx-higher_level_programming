#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance of the specified class
"""

def is_same_class(obj, a_class):
	""" prints true if object is an instance, false if it is an subclass

	Args:
	     obj(any): the object to check
	     a_class(type): the class to check obj with

 	Returns:
	      True if the obj is an instance of a_class
	      False if otherwise
	"""

        print(isinstance(obj,a_class))

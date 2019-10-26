"""
Tests for Webster 1.0
"""

from webster_py import *

def test(name, expected, value):
	"""
	Tests if a given value is equivalent to the expected value
	Example Usage: test("concatenation", hello", "he" + "llo")
	Returns true if the test passed, false otherwise
	"""

	if expected == value:
		resultstr = "PASSED"
		resultbool = True
	else:
		resultstr = "FAILED"
		resultbool = False
	print("Testing", name + ":", resultstr)
	print("\tExpected:", expected)
	print("\tResult:", value)
	return resultbool

def test_list(tests):
	"""
	Tests should contain a list of tuples
	The first element of the tuple should be the name
	The second element should be the expected value
	The third element should be the actual value
	Returns the number of tests that failed
	"""

	fails = 0
	for tst in tests:
		 if not test(tst[0], tst[1], tst[2]):
		 	fails += 1

def result_type_enum():

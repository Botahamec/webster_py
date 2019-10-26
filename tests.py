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

def rule_type_enum():
	test("RuleType Is", RuleType.IS, RuleType.IS)

def 

def run_all_tests():
	rule_type_enum()

if __name__ == "__main__":
	run_all_tests()
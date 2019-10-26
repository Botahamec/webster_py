"""
Tests for Webster 1.0
"""

from webster_py import *

def test(name, result, expected):
	"""
	Tests if a given value is equivalent to the expected value
	Example Usage: test("concatenation", hello", "he" + "llo")
	Returns true if the test passed, false otherwise
	"""

	if result == expected:
		print("Testing", name + ": PASSED")
		return True
	else:
		print("Testing", name + ": FAILED")
		print("\tExpected:", expected)
		print("\tResult:", result)
		return False

# tests RuleType enumerator
def rule_type_enum():
	test("RuleType Is", RuleType.IS, RuleType.IS)

# tests Rule.__init__()
def init_rule():
	rule = Rule(RuleType.GREATER, 5)
	test("Rule Construction Type", rule.rule_type, RuleType.GREATER)
	test("Rule Construction Value", rule.value, 5)

# tests Rule.match(value)
def rule_match():
	test("Rule IS", Rule(RuleType.IS, "Hello").match("Hello"), True)
	test("Rule IS Failure", Rule(RuleType.IS, "Hello").match("World"), False)
	greater_rule = Rule(RuleType.GREATER, 3)
	test("Rule GREATER", greater_rule.match(5), True)
	test("Rule GREATER Failure", Rule(RuleType.GREATER, 3).match(1), False)
	less_rule = Rule(RuleType.LESS, 10)
	test("Rule LESS", less_rule.match(1), True)
	test("Rule LESS Failure", less_rule.match(12), False)
	and_rule = Rule(RuleType.AND, [greater_rule, less_rule])
	test("Rule AND", and_rule.match(7), True)
	test("Rule AND Failure 1", and_rule.match(0), False)
	test("Rule AND Failure 2", and_rule.match(15), False)
	or_rule = Rule(RuleType.OR, [Rule(RuleType.IS, 3), greater_rule])
	test("Rule OR 1", or_rule.match(3), True)
	test("Rule OR 2", or_rule.match(5), True)
	test("Rule OR Failure", or_rule.match(-3), False)
	contain_rule = Rule(RuleType.CONTAIN, 'h')
	test("Rule CONTAINS", contain_rule.match("hello"), True)
	test("Rule CONTAINS Failure", contain_rule.match("world"), False)
	xor_rule = Rule(RuleType.XOR, [contain_rule, Rule(RuleType.CONTAIN, 'o')])
	test("Rule XOR 1", xor_rule.match("world"), True)
	test("Rule XOR 2", xor_rule.match("help"), True)
	test("Rule XOR Failure 1", xor_rule.match("hello"), False)
	test("Rule XOR Failure 2", xor_rule.match("animal"), False)
	not_rule = Rule(RuleType.NOT, Rule(RuleType.IS, 6))
	test("Rule NOT", not_rule.match(3), True)
	test("Rule NOT Failure", not_rule.match(6), False)

def run_all_tests():
	rule_type_enum()
	init_rule()
	rule_match()

if __name__ == "__main__":
	run_all_tests()

"""
A series of tests for Webster 0.3's Rule class
Designed to run with UnitTest
"""

from webster import *
import unittest

class TestRule(unittest.TestCase):

	def test_init(self):
		rule = Rule(RuleType.IS, Value(ValueType.NEW, 6), Value(ValueType.NEW, 3))
		self.assertEqual(rule.rule_type, RuleType.IS)
		self.assertEqual(rule.value1, Value(ValueType.NEW, 6))
		self.assertEqual(rule.value2, Value(ValueType.NEW, 3))

	def test_eq(self):
		rule = Rule(RuleType.IS, Value(ValueType.NEW, 6), Value(ValueType.NEW, 3))
		self.assertEqual(rule, Rule(RuleType.IS, Value(ValueType.NEW, 6), Value(ValueType.NEW, 3)))

	def test_match(self):

		self.assertTrue(Rule(RuleType.IS, Value(ValueType.NEW, 6), Value(ValueType.NEW, 6)).match())
		self.assertTrue(Rule(RuleType.IS, Value(ValueType.NEW, 6), Value(ValueType.OPERATE, Operation(OperationType.ADD, Value(ValueType.NEW, 3), Value(ValueType.NEW, 3)))).match())
		self.assertFalse(Rule(RuleType.IS, Value(ValueType.NEW, 6), Value(ValueType.NEW, 3)).match())

		self.assertTrue(Rule(RuleType.GREATER, Value(ValueType.NEW, 6), Value(ValueType.NEW, 8)).match())
		self.assertFalse(Rule(RuleType.GREATER, Value(ValueType.NEW, 6), Value(ValueType.NEW, 2)).match())
		self.assertFalse(Rule(RuleType.GREATER, Value(ValueType.NEW, 6), Value(ValueType.NEW, 6)).match())

		self.assertTrue(Rule(RuleType.LESS, Value(ValueType.NEW, 9), Value(ValueType.NEW, 5)).match())
		self.assertFalse(Rule(RuleType.LESS, Value(ValueType.NEW, 9), Value(ValueType.NEW, 12)).match())
		self.assertFalse(Rule(RuleType.LESS, Value(ValueType.NEW, 9), Value(ValueType.NEW, 9)).match())

		self.assertTrue(Rule(RuleType.AND, Value(ValueType.NEW, Rule(RuleType.GREATER, Value(ValueType.NEW, 6), Value(ValueType.NEW, 8))), Value(ValueType.NEW, Rule(RuleType.LESS, Value(ValueType.NEW, 9), Value(ValueType.NEW, 8)))).match())
		self.assertFalse(Rule(RuleType.AND, Value(ValueType.NEW, Rule(RuleType.GREATER, Value(ValueType.NEW, 6), Value(ValueType.NEW, 9))), Value(ValueType.NEW, Rule(RuleType.LESS, Value(ValueType.NEW, 9), Value(ValueType.NEW, 9)))).match())
		self.assertFalse(Rule(RuleType.AND, Value(ValueType.NEW, Rule(RuleType.GREATER, Value(ValueType.NEW, 6), Value(ValueType.NEW, 2))), Value(ValueType.NEW, Rule(RuleType.LESS, Value(ValueType.NEW, 9), Value(ValueType.NEW, 2)))).match())

		# TODO: fix the rest of these tests

		"""
		orrule = Rule(RuleType.OR, Value(ValueType.NEW, [isrule, gtrule]))
		self.assertTrue(orrule.match(Value(ValueType.NEW, 6)))
		self.assertTrue(orrule.match(Value(ValueType.NEW, 9)))
		self.assertFalse(orrule.match(Value(ValueType.NEW, 3)))

		xorrule = Rule(RuleType.XOR, Value(ValueType.NEW, [Rule(RuleType.CONTAIN, Value(ValueType.NEW, 'o')), Rule(RuleType.CONTAIN, Value(ValueType.NEW, 'e'))]))
		self.assertTrue(xorrule.match(Value(ValueType.NEW, "Hey")))
		self.assertTrue(xorrule.match(Value(ValueType.NEW, "o!")))
		self.assertFalse(xorrule.match(Value(ValueType.NEW, "Hi")))
		self.assertFalse(xorrule.match(Value(ValueType.NEW, "Hello")))

		notrule = Rule(RuleType.NOT, Value(ValueType.NEW, Rule(RuleType.IS, Value(ValueType.NEW, 5))))
		self.assertTrue(notrule.match(Value(ValueType.NEW, 3)))
		self.assertFalse(notrule.match(Value(ValueType.NEW, 5)))

		contain = Rule(RuleType.CONTAIN, Value(ValueType.NEW, 'o'))
		self.assertTrue(contain.match(Value(ValueType.NEW, "Hello")))
		self.assertFalse(contain.match(Value(ValueType.NEW, "Bye!")))

		anyrule = Rule(RuleType.ANY, Value(ValueType.NEW, Rule(RuleType.LESS, Value(ValueType.NEW, 3))))
		self.assertTrue(anyrule.match(Value(ValueType.NEW, [1, 2, 3, 4, 5])))
		self.assertFalse(anyrule.match(Value(ValueType.NEW, [3, 4, 5, 6])))
		"""
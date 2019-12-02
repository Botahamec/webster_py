"""
A series of tests for Webster 0.3's Value class
Designed to run with UnitTest
"""

from webster import *
import unittest

class TestDefinition(unittest.TestCase):

	def test_init(self):
		definition = Definition("Apple", Rule(RuleType.IS, Value(ValueType.ATTR, "color"), Value(ValueType.NEW, "red")))
		self.assertEqual(definition.name, "Apple")
		self.assertEqual(definition.rule, Rule(RuleType.IS, Value(ValueType.ATTR, "color"), Value(ValueType.NEW, "red")))

	def test_eq(self):
		definition = Definition("Apple", Rule(RuleType.IS, Value(ValueType.ATTR, "color"), Value(ValueType.NEW, "red")))
		Definition("Apple", Rule(RuleType.IS, Value(ValueType.ATTR, "color"), Value(ValueType.NEW, "red")))
		self.assertEqual(definition, Definition("Apple", Rule(RuleType.IS, Value(ValueType.ATTR, "color"), Value(ValueType.NEW, "red"))))
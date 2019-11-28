"""
A series of tests for Webster 0.3's Value class
Designed to run with UnitTest
"""

from webster import *
import unittest

class TestValue(unittest.TestCase):

	def test_init(self):
		value = Value(ValueType.NEW, 5)
		self.assertEqual(value.value_type, ValueType.NEW)
		self.assertEqual(value.helper_value, 5)

	def test_equal(self):
		value = Value(ValueType.NEW, 5)
		self.assertEqual(value, Value(ValueType.NEW, 5))
		self.assertNotEqual(value, Value(ValueType.ATTR, 5))
		self.assertNotEqual(value, Value(ValueType.NEW, 6))

	def test_new(self):
		value = Value(ValueType.NEW, 5)
		self.assertEqual(value.value(), 5)
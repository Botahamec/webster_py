"""
A series of tests for Webster 0.3's Value class
Designed to run with UnitTest
"""

from webster import *
import unittest

class TestOperation(unittest.TestCase):

	def test_init(self):
		op = Operation(OperationType.ADD, Value(ValueType.NEW, 2), Value(ValueType.NEW, 3))
		self.assertEqual(op.op_type, OperationType.ADD)
		self.assertEqual(op.value1, Value(ValueType.NEW, 2))
		self.assertEqual(op.value2, Value(ValueType.NEW, 3))

	def test_eq(self):
		op = Operation(OperationType.ADD, Value(ValueType.NEW, 2), Value(ValueType.NEW, 3))
		self.assertEqual(op, Operation(OperationType.ADD, Value(ValueType.NEW, 2), Value(ValueType.NEW, 3)))
		self.assertNotEqual(op, Operation(OperationType.SUB, Value(ValueType.NEW, 2), Value(ValueType.NEW, 3)))
		self.assertNotEqual(op, Operation(OperationType.ADD, Value(ValueType.NEW, 3), Value(ValueType.NEW, 3)))

	def test_perform(self):

		add = Operation(OperationType.ADD, Value(ValueType.NEW, 2), Value(ValueType.NEW, 3))
		self.assertEqual(add.perform(), 5)

		sub = Operation(OperationType.SUB, Value(ValueType.NEW, 5), Value(ValueType.NEW, 2))
		self.assertEqual(sub.perform(), 3)

		mul = Operation(OperationType.MULT, Value(ValueType.NEW, 3), Value(ValueType.NEW, 2))
		self.assertEqual(mul.perform(), 6)

		div = Operation(OperationType.DIV, Value(ValueType.NEW, 6), Value(ValueType.NEW, 3))
		self.assertEqual(div.perform(), 2)

		push = Operation(OperationType.PUSH, Value(ValueType.NEW, [1, 2]), Value(ValueType.NEW, 3))
		self.assertEqual(push.perform(), [1, 2, 3])

		pop = Operation(OperationType.POP, Value(ValueType.NEW, [1, 2]), Value(ValueType.NEW, None))
		self.assertEqual(pop.perform(), [1])

		con = Operation(OperationType.CONCAT, Value(ValueType.NEW, [1, 2]), Value(ValueType.NEW, [3, 4]))
		self.assertEqual(con.perform(), [1,2,3,4])

		ind = Operation(OperationType.INDEX, Value(ValueType.NEW, [1, 2, 3, 4]), Value(ValueType.NEW, 2))
		self.assertEqual(ind.perform(), 3)

		rem = Operation(OperationType.REMOVE, Value(ValueType.NEW, [1,2,3,4]), Value(ValueType.NEW, 2))
		self.assertEqual(rem.perform(), [1,2,4])

	def test_value(self):
		add = Operation(OperationType.ADD, Value(ValueType.NEW, 2), Value(ValueType.NEW, 3))
		self.assertEqual(add.value(), Value(ValueType.NEW, 5))
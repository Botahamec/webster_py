
from enum import Enum

class ValueType(Enum):
	"""
	Indicates where to get the value from
	"""

	NEW     = 0 # create a new value whizh is equal to a specific value
	ATTR    = 1 # get the value of an attribute of the current thing
	OPERATE = 2 # use the value returned by an operation
	RULE    = 3 # use the boolean value returned by a rule

class Value:
	"""
	A value for a rule or an operation
	"""

	def __init__(self, value_type: ValueType, helper_value: any) -> "Value":
		"""
		Constructor for a Value

		Arguments:
			value_type {ValueType} -- The method to use in deriving the value
			helper_value {any} -- The object that'll be used to derive the value

		Here's a table for what helper_value's type must be depending on value_type
		VALUE_TYPE | HELPER_VALUE TYPE | DESCRIPTION
		--------------------------------------------
		NEW        | Any               | The actual value
		ATTR       | String            | The Attribute of the Thing to use
		OPERATE    | Operation         | The Operation to calculate to get the value
		RULE       | Rule              | The Rule to test
		"""

		self.value_type = value_type
		self.helper_value = helper_value

	def __eq__(self, other: "Value") -> bool:
		"""
		Checks to see if two Values are equal

		Raises:
			TypeError: tried to compare a Value to something that isn't a Value

		Returns:
			bool -- whether or not they are not equal
		"""

		if not isinstance(other, Value):
			raise TypeError("can only compare two Values")
		else:
			return self.value_type == other.value_type and \
				self.helper_value == other.helper_value

	def value(self, thing=None):
		"""
		Returns the actual value

		Arguments:
			thing {Thing} -- the Thing to use in determining the value

		Returns:
			Any -- the value
		"""

		if self.value_type == ValueType.NEW:
			return self.helper_value

		# TODO: implement ValueType.ATTR
		elif self.value_type == ValueType.ATTR:
			pass

		# TODO: implement ValueType.OPERATE
		elif self.value_type == ValueType.OPERATE:
			pass

		# TODO: implement ValueType.RULE
		elif self.value_type == ValueType.RULE:
			pass

class OperationType(Enum):
	"""
	Indicates which operation to perform
	"""

	ADD     = 0
	SUB     = 1
	MULT    = 2
	DIV     = 3
	MOD     = 4
	PUSH    = 5
	POP     = 6
	CONCAT  = 7
	INDEX   = 8
	REMOVE  = 9
	MAP     = 10
	FILTER  = 11
	FOREACH = 12
	REPEAT  = 13

class Operation:
	"""
	An operation to perform
	"""

	def __init__(self, op_type, value1, value2) -> "Operation":
		"""
		Creates an Operation object

		Arguments:
			op_type {OperationType} -- The operation to perform
			value1 {Value} -- The first parameter of the operation
			value2 {Value} -- The second parameter of the operation
		"""

		self.op_type = op_type
		self.value1 = value1
		self.value2 = value2

	def __eq__(self, other: "Operation") -> bool:
		if not isinstance(other, Value):
			raise TypeError("can only compare two Values")
		else:
			return self.op_type == other.op_type and \
				self.value1 == other.value1 and self.value2 == self.value2

	def perform(self, thing=None):

		if self.op_type == OperationType.ADD:
			return self.value1 + self.value2
		elif self.op_type == OperationType.SUB:
			return self.value1 - self.value2
		elif self.op_type == OperationType.MULT:
			return self.value1 * self.value2
		elif self.op_type == OperationType.DIV:
			return self.value1 / self.value2
		elif self.op_type == OperationType.PUSH:
			return self.value1 + [self.value2]
		elif self.op_type == OperationType.POP:
			return self.value1.pop()
		elif self.op_type == OperationType.CONCAT:
			return self.value1 + self.value2
		elif self.op_type == OperationType.INDEX:
			return self.value1[self.value2]
		elif self.op_type == OperationType.REMOVE:
			return self.value1.pop(obj=self.value2)

		# TODO: implement MAP, FILTER, FOREACH, REPEAT
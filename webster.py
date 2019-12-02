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

	VALUE_TYPE | HELPER_VALUE TYPE | DESCRIPTION
	--------------------------------------------
	NEW        | Any               | The actual value
	ATTR       | String            | The Attribute of the Thing to use
	OPERATE    | Operation         | The Operation to calculate to get the value
	RULE       | Rule              | The Rule to test
	"""

	def __init__(self, value_type: ValueType, helper_value: any) -> "Value":
		"""
		Constructor for a Value

		Arguments:
			value_type {ValueType} -- The method to use in deriving the value
			helper_value {any} -- The object that'll be used to derive the value
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
			return TypeError("can only compare two Values")
		else:
			return self.value_type == other.value_type and \
				self.helper_value == other.helper_value

	def value(self, thing=None) -> any:
		"""
		Returns the actual value

		Arguments:
			thing {Thing} -- the Thing to use in determining the value (default: {None})

		Returns:
			Any -- the value
		"""

		if self.value_type == ValueType.NEW:
			return self.helper_value

		# TODO: implement ValueType.ATTR
		elif self.value_type == ValueType.ATTR:
			pass

		elif self.value_type == ValueType.OPERATE:
			return self.helper_value.perform()

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

	OPERATION | VALUE1_TYPE | VALUE2_TYPE | DESCRIPTION
	---------------------------------------------------
	ADD       | Number      | Number      | Adds the numbers together
	SUB       | Number      | Number      | Subtracts two numbers
	MULT      | Number      | Number      | Multiplies
	DIV       | Number      | Number      | Divides
	MOD       | Number      | Number      | Modulo
	PUSH      | List        | Any         | Pushes to a list
	POP       | List        | Any         | Pops the last value off
	CONCAT    | List        | List        | Concatenates th two lists
	INDEX     | List        | Number      | Gets the value at the specified index
	REMOVE    | List        | Number      | Removes the number at the specified index
	"""

	def __init__(self, op_type: OperationType, value1: Value, value2: Value) -> "Operation":
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
		if not isinstance(other, Operation):
			raise TypeError("can only compare two Operations")
		else:
			return self.op_type == other.op_type and \
				self.value1 == other.value1 and self.value2 == self.value2

	def perform(self, thing=None) -> any:
		"""
		Returns the result of the operation

		Keyword Arguments:
			thing {Thing} -- The thing to perform the operation on (default: {None})

		Returns:
			any -- the result of the operation
		"""

		if self.op_type == OperationType.ADD:
			return self.value1.value(thing=thing) + self.value2.value(thing=thing)
		elif self.op_type == OperationType.SUB:
			return self.value1.value(thing=thing) - self.value2.value(thing=thing)
		elif self.op_type == OperationType.MULT:
			return self.value1.value(thing=thing) * self.value2.value(thing=thing)
		elif self.op_type == OperationType.DIV:
			return self.value1.value(thing=thing) / self.value2.value(thing=thing)
		elif self.op_type == OperationType.PUSH:
			return self.value1.value(thing=thing) + [self.value2.value(thing=thing)]
		elif self.op_type == OperationType.POP:
			return self.value1.value(thing=thing)[:-1]
		elif self.op_type == OperationType.CONCAT:
			return self.value1.value(thing=thing) + self.value2.value(thing=thing)
		elif self.op_type == OperationType.INDEX:
			return self.value1.value(thing=thing)[self.value2.value(thing=thing)]
		elif self.op_type == OperationType.REMOVE:
			lst = self.value1.value(thing=thing)
			lst.pop(self.value2.value(thing=thing))
			return lst

		# TODO: implement MAP, FILTER, FOREACH, REPEAT

	def value(self, thing=None) -> Value:
		"""
		A value containing the result of the operation

		Keyword Arguments:
			thing {Thing} -- The thing to perform the operation on (default: {None})

		Returns:
			Value -- the resultant value
		"""
		return Value(ValueType.NEW, self.perform(thing))

class RuleType(Enum):
	IS      = 0
	GREATER = 1
	LESS    = 2
	AND     = 3
	OR      = 4
	XOR     = 5
	NOT     = 6
	CONTAIN = 7
	ANY     = 8

class Rule:
	"""
	Contains a RuleType and a value

	RuleType | Value1     | Description
	------------------------------------
	IS       | any        | The value in the thing == the value in the rule
	GREATER  | number     | The value in the thing > the value in the rule
	LESS     | number     | The value in the thing < than the value in the rule
	AND      | rule list  | All rules specified are true
	OR       | rule list  | Any of the rules specified are true
	XOR      | rule list  | One of the rules specified are true
	NOT      | rule       | The specified rule is false
	CONTAIN  | any        | A list contains the specified value
	ANY      | rule       | The list has a value which follows the rule
	"""

	def __init__(self, rule_type: RuleType, value1: Value, value2: Value) -> "Rule":
		"""
		Constructor

		Arguments:
			rule_type {RuleType} -- The type of Rule
			value1 {Value} -- The first value to use
			value2 {Value} -- The second value
		"""

		self.rule_type = rule_type
		self.value1 = value1
		self.value2 = value2

	def __eq__(self, other: "Rule") -> bool:
		"""
		Checks if two Rules are equal

		Arguments:
			other {Rule} -- the Rule to compare to

		Returns:
			bool -- whether or not the values are equal
		"""

		if not isinstance(other, Rule):
			# don't attempt to compare against unrelated types
			return NotImplemented
		return self.rule_type == other.rule_type and self.value1 == other.value1 and self.value2 == other.value2

	def match(self, thing=None) -> bool:
		"""
		Checks if a value matches the Rule

		Arguments:
			value {Value} -- A Value to check

		Keyword Arguments:
			thing {Thing} -- The Thing to use when determining the value (default: {None})

		Returns:
			bool -- returns True if the value matches
		"""

		if self.rule_type == RuleType.IS: return self.value2.value(thing=thing) == self.value1.value(thing=thing)
		elif self.rule_type == RuleType.GREATER: return self.value2.value(thing=thing) > self.value1.value(thing=thing)
		elif self.rule_type == RuleType.LESS: return self.value2.value(thing=thing) < self.value1.value(thing=thing)
		elif self.rule_type == RuleType.AND:
			return self.value1.value(thing=thing).match(thing=Thing) and \
				self.value2.value(thing=Thing).match(thing=Thing)
		elif self.rule_type == RuleType.OR:
			for rule in self.value1.value(thing=thing):
				if rule.match(self.value2): return True
			return False
		elif self.rule_type == RuleType.XOR:
			checks = 0
			for rule in self.value1.value(thing=thing):
				if rule.match(self.value2): checks += 1
				if checks > 1: return False
			if checks == 1: return True
			return False
		elif self.rule_type == RuleType.NOT: return not self.value1.value(thing=thing).match(self.value2)
		elif self.rule_type == RuleType.CONTAIN: return self.value1.value(thing=thing) in self.value2.value(thing=thing)
		elif self.rule_type == RuleType.ANY:
			for item in self.value2.value(thing=thing):
				if self.value1.value(thing=thing).match(Value(ValueType.NEW, item)): return True
			return False

class Definition:
	"""
	A name attached to a Rule
	"""

	def __init__(self, name: str, rule: Rule):
		"""
		Constructor

		Arguments:
			name {str} -- The name of the definition
			rule {Rule} -- The Rule for determining if a Thing matches the Definition
		"""
		self.name = name
		self.rule = rule

	def __eq__(self, other: "Definition") -> bool:
		"""
		Checks to see if two definitions are equal

		Arguments:
			other {Definition} -- The Definition to compare to

		Returns:
			bool -- True if the definitions are equal
		"""

		if not isinstance(other, Definition):
			# don't attempt to compare against unrelated types
			return NotImplemented
		return self.name == other.name and self.rule == other.rule

class Thing:
	"""
	A name attached to a bunch of properties
	"""

	def __init__(self, name: str, properties: dict, definition=None) -> "Thing":

		self.name = name
		self.properties = properties
		if defined is not None:
			self.defined = True
		else:
			self.defined = False
		self.definition = definition

	def __eq__(self, other: "Thing") -> bool:
		"""
		Checks to see if two Things are equal

		Arguments:
			other {Thing} -- The Thing to compare to

		Returns:
			bool -- True if the Things are equal
		"""

		if not isinstance(other, Thing):
			# don't attempt to compare against unrelated types
			return NotImplemented
		return self.name == other.name and self.properties == other.properties
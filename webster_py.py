"""
Webster is a framework which I hope to use for AI in the future

classes:
	Rule
	Property
	Definition
	Thing
	Webster
"""

from enum import Enum

class RuleType(Enum):
	IS      = 0
	GREATER = 1
	LESS    = 2
	AND     = 3
	OR      = 4
	XOR     = 5
	NOT     = 6
	CONTAIN = 7

class Rule:
	"""
	Contains a RuleType and a value

	RuleType | Value Type | Description
	------------------------------------
	IS       | any        | The value in the thing == the value in the rule
	GREATER  | number     | The value in the thing > the value in the rule
	LESS     | number     | The value in the thing < than the value in the rule
	AND      | rule list  | All rules specified are true
	OR       | rule list  | Any of the rules specified are true
	XOR      | rule list  | One of the rules specified are true
	NOT      | rule       | The specified rule is false
	CONTAIN  | any        | A list contains the specified value
	"""

	def __init__(self, rule_type: RuleType, value: any):
		"""
		Example usage: Rule(RuleType.IS, "Hello!")
		"""

		self.rule_type = rule_type
		self.value = value
	
	def match(self, value: any) -> bool:
		"""
		Checks to see if the given value obeys the rule
		Returns true if it does, false otherwise
		"""

		if self.rule_type == RuleType.IS: return value == self.value
		elif self.rule_type == RuleType.GREATER: return value > self.value
		elif self.rule_type == RuleType.LESS: return value < self.value
		elif self.rule_type == RuleType.AND:
			for rule in self.value:
				if not rule.match(value): return False
			return True
		elif self.rule_type == RuleType.OR:
			for rule in self.value:
				if rule.match(value): return True
			return False
		elif self.rule_type == RuleType.XOR:
			checks = 0
			for rule in self.value:
				if rule.match(value): checks += 1
				if checks > 1: return False
			if checks == 1: return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
			return False
		elif self.rule_type == RuleType.NOT: return not self.value.match(value)
		elif self.rule_type == RuleType.CONTAIN: return self.value in value
		raise "No valid RuleType found for this Rule"

class Property:
	"""
	Attaches a name to a rule, which may contain other rules
	"""

	def __init__(self, name: str, rule: Rule):
		self.name = name
		self.rule = rule
	
	def match(self, value: any) -> bool:
		"""
		Returns true if the value satisfies the property
		Returns false otherwise
		"""
		return self.rule.match(value)

class Definition:
	"""
	Essentially a name linked to a dictionary of properties
	All properties must match a given thing for it to match the definition
	"""

	def __init__(self, name: str, props):
		"""
		name: the name of the definition
		props: a list of properties, which will be converted to a dictionary
		"""
		self.name = name
		self.props = {}
		for prop in props:
			self.props[prop.name] = prop
	
	def match(self, thing) -> bool:
		"""
		Returns true if the definition is a match, false otherwise
		A thing must match all properties to match the definition
		It also satisfies the definition is it's already defined as doing so
		"""
		if thing.definition == self.name:
			return True
		for prop in self.props:
			if prop.name in thing.attrs:
				if not prop.match(thing.attrs[prop.name]):
					return False
			else:
				return False
		return True

class Thing:
	"""
	An object which is known to exist
	Has an id and a dictionary of attributes
	"""

	def __init__(self, identifier, attributes = None, definition = None):
		"""
		identifier: An ID for the thing
		props: a list of properties for the Thing
		definition: the name of the definition for the thing
		"""
		self.identifier = identifier
		self.definition = None
		if definition != None:
			self.definition = definition
		if attributes == None:
			self.attrs = {}
		else:
			self.attrs = attributes

"""
Webster is a framework which I hope to use for AI in the future

classes:
	Rule
	Property
	Definition
	Thing
	Webster

rules:
	is
	greater
	less
	and
	or
	xor
	not
	contain
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

	def __init__(rule_type: int, value: any):
		"""
		Example usage: Rule(RuleType.IS, "Hello!")
		"""

		self.rule_type = rule_type
		self.value = value

class Property:

	def __init__(name: str, rule: Rule):
		self.name = name
		self.rule = rule
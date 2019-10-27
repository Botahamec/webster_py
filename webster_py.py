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
	

	def __eq__(self, other):
		if not isinstance(other, Rule):
			# don't attempt to compare against unrelated types
			return NotImplemented
		return self.rule_type == other.rule_type and self.value == other.value

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
	
	def __eq__(self, other):
		if not isinstance(other, Property):
			# don't attempt to compare against unrelated types
			return NotImplemented
		return self.name == other.name and self.rule == other.rule
	
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
	
	def __eq__(self, other):
		if not isinstance(other, Definition):
			# don't attempt to compare against unrelated types
			return NotImplemented
		return self.name == other.name and self.props == other.props

	def match(self, thing) -> bool:
		"""
		Returns true if the definition is a match, false otherwise
		A thing must match all properties to match the definition
		It also satisfies the definition is it's already defined as doing so
		"""

		if thing.definition == self.name:
			return True
		for prop in self.props:
			if prop in thing.attrs:
				if not self.props[prop].match(thing.attrs[prop]):
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
	
	def __eq__(self, other):
		if not isinstance(other, Thing):
			# don't attempt to compare against unrelated types
			return NotImplemented
		ident_eq = self.identifier == other.identifier
		attrs_eq = self.attrs == other.attrs
		defin_eq = self.definition == other.definition
		return ident_eq and attrs_eq and defin_eq

class Webster:
	"""
	A container for all the information
	Contains a hashmap for its brain and dictionary
	The brain contains things while the dictionary contains definitions
	"""

	def __init__(self, brain = None, dictionary = None):
		"""
		Brain and dictionary are both lists
		They contain things and definitions, respectively
		"""

		self.brain = {}
		if brain != None:
			for thing in brain:
				self.brain[thing.identifier] = thing
		self.dictionary = {}
		if dictionary != None:
			for definition in dictionary:
				self.dictionary[definition.name] = definition
	
	def __eq__(self, other):
		if not isinstance(other, Webster):
			# don't attempt to compare against unrelated types
			return NotImplemented
		brain = self.brain
		dictionary = self.dictionary
		return brain == other.brain and dictionary == other.dictionary
	
	def get_definition(self, name: str) -> Definition:
		"""
		Gets a definition from the dictionary from its name
		"""

		return self.dictionary[name]
	
	def get_thing(self, identifier: str) -> Thing:
		"""
		Gets a definition from the brain based on its identifier
		"""

		return self.brain[identifier]
	
	def add_definition(self, name: str, props) -> Definition:
		"""
		Adds a definition to the dictionary
		Returns the new definition
		"""

		new_def = Definition(name, props)
		self.dictionary[name] = new_def
		return new_def
	
	def add_thing(self, identifier, attributes=None, definition=None) -> Thing:
		"""
		Adds a thing to the brain
		Returns the new thing
		"""

		new_thing = Thing(identifier,
							attributes=attributes,
							definition=definition)
		self.brain[identifier] = new_thing
		return new_thing
	
	def get_property(self, definition: str, property: str) -> Property:
		"""
		Returns a Property
		definition: The name of the definition to pull from
		property: The name of the property to return
		"""

		return self.dictionary[definition].props[property]
	
	def get_rule(self, definition: str, property: str) -> Rule:
		"""
		Returns the rule associated with the specified property
		definition: The name of the definition to pull from
		property: The name of the property to pull from
		"""

		return self.dictionary[definition].props[property].rule

	def get_attribute(self, identifier, attribute: str):
		"""
		Returns the value of a Thing
		identifier: the ID of the Thing
		attribute: The name of the attribute
		"""

		return self.brain[identifier].attrs[attribute]
	
	def set_property_rule(self, definition: str, property: str, rule: Rule):
		"""
		Sets a rule for a given property
		definition: The name of the definition
		property: The name of the property to be changed
		rule: The new rule
		Returns the rule given
		"""

		self.dictionary[definition].props[property].rule = rule
		return rule
	
	def add_property(self, definition: str, name: str, rule: Rule) -> Property:
		"""
		Creates a new property and adds it to the given definition
		definition: The name of the definition
		name: The name of the property
		rule: The rule for the property
		"""

		new_prop = Property(name, rule)
		self.dictionary[definition].props[name] = new_prop
		return new_prop
	
	def set_attribute(self, thing, name: str, value: any) -> str:
		"""
		Sets the value of an attribute for a Thing
		thing: The ID of the Thing to modify
		name: The name of the attribute
		value: The value of the attribute
		"""

		self.brain[thing].attrs[name] = value
		return name
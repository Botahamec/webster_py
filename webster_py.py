
# a definition or an object
class Object:
	"""
	An object can be either a definition or an actual object in Webster's memory.
	An object contains properties and possible applying adjectives.
	"""

	def __init__(self, name, properties):
		"""
		This is the constructor for the object type.
		The name is how the object will be identified.
		The properties is a dictionary of names for the properties, and the value of it.
		"""

		self.name = name # the name of the definition, or the id of the object
		self.properties = properties # a dictionary containing the name of the property and a value describing it

# the webster bot
class Webster:
	"""
	This object contains the actual Webster bot.
	A Webster object has two properties: the dictionary and the memory.
	The dictionary contains all of the possible types of objects which exist.
	The memory lists all of the objects which Webster knows exist.
	"""

	def __init__(self):
		"""
		This is the constuctor for the Webster object.
		It doesn't take any particular properties.
		It creates the dictionary and memory arrays
		"""

		self.memory = [] # an array of all the objects which exist
		self.dictionary = [] # an array of all the objects which could exist
	
	def add_definition(self, name, properties):
		"""
		This function creates a new definition.
		"""
		self.dictionary.append(Object(name, properties)) # pretty much just calls the Object constructor
	
	def get_definition(self, name):
		"""
		This function looks through the dictionary to find a definition with the name given.
		"""

		for definition in self.dictionary:
			if definition.name == name: return definition
		raise Exception("no object of the given name found")
	
	def add_object(self, id, definition):
		"""
		This function adds a new object to the memory.
		This requires that a definition of the object already exists.
		The object constructor is called and the object is given the properties of the definition referenced.
		"""

		self.memory.append(Object(id, self.get_definition(definition).properties))
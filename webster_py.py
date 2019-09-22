
# a definition or an object
class Object:
	"""
	An object can be either a definition or actual object in Webster's memory.
	An object contains properties and possible applying adjectives.
	"""

	def __init__(self, name, properties):
		"""
		This is the constructor for the object type.
		The name is how the object will be identified.
		The properties is a dictionary of nproperties.
		"""

		self.name = name # the name of the definition, or the id of the object
		self.properties = properties # a dictionary containing the properties

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
		name: The name of the definition
		properties: The dictionary of properties to be added to the definition
		"""
		self.dictionary.append(Object(name, properties)) # Object constructor
	
	def get_definition(self, name):
		"""
		looks through the dictionary to find a definition with the name
		"""

		for definition in self.dictionary: # checks each definition in the dict
			if definition.name == name: return definition # returns definition
		raise Exception("no object of the given name found") # if none found
	
	def add_object(self, id, definition):
		"""
		This function adds a new object to the memory.
		This requires that a definition of the object already exists.
		The object is given the properties of the definition referenced.
		"""

		properties = self.get_definition(definition).properties # properties
		self.memory.append(Object(id, properties)) # calls object constructor
	
	def get_object(self, id):
		"""
		This function gets an object from memory with the specified id
		"""

		for object in self.memory: # checks the id of each object
			if object.name == id: return object # returns one with correct id
		raise Exception("no object of the given id found") # if none found

	def _get_object_index(self, id):
		"""
		This function returns index of an object with given id in the memory
		Not meant to be used by users, only by the Webster object
		"""

		for index in range(0, len(self.memory)): # checks id of each object
			if self.memory[index].name == id: return index # returns index
		raise Exception("no object of the given id found") # if none found

	def _get_definition_index(self, name):
		"""
		This function returns index of a dictionay with the given name
		This function should only be used by the Webster object
		"""

		for index in range(0, len(self.dictionary)): # checks each definition
			if self.dictionary[index].name == name: return index # reurns index
		raise Exception("no object of the given id found") # if none found

	def get_object_property(self, object_id, property):
		"""
		This function returns the value of a property in a given object.
		"""

		object = self.get_object(object_id) # the object with the given name
		for name, value in object.properties.items(): # checks all properties
			if name == property: return value # returns the value
		raise Exception("No property of the given name found") # if none found

	def get_definition_property(self, definition_name, property):
		"""
		This function returns the value of a property in a given definition
		"""

		definition = self.get_definition(definition_name) # the definition
		for name, value in definition.properties.items(): # checks properties
			if name == property: return value # returns the value
		raise Exception("No property of the given name found") # if none found

	def definition_of_type(self, new_name, og_def):
		"""
		This function creates a new definition with the properties of another
		This is useful for inheritance
		"""
		properties = self.get_definition(og_def).properties  # new properties
		self.add_definition(new_name, properties)  # creates new definition

"""
Webster is a framework which will in the future be used for AI
Currently is not very useful other than being used to store known information
The definitions are currently the same as the actual objects, which isn't good
However, I will call this 1.0, because it does most of what I expect 1.0 to do
The problem is that the rest of what I want it to do in unpractical
It's supposed to used an advanced version of dynamic typing
Changing definitions should be able to change the value of objects in memory
But this doesn't make much sense to implement
Imagine I learned that emeralds are green but I thought rubies were emeralds
I wouldn't then conclude that rubies are green
I'd just say that rubies aren't emeralds
Anyway, here's a list of features I'll add in the future to make it better
-------------------------------------------------------------------------------
Definitions and Objects need to be separate classes
There needs to be a special DictionaryProperty class
The DictionaryProperty class will be much more robust
It will contain a binary operator, which an object will need to fulfill
Dictionaries should also have a list of digital "makefiles"
The makefiles should help the objects figure out their own properties
Definitions also should have a list of adjectives
Adjectives are boolean functions which are based on the object's properties
This requires a digital "programming language"
That's a completely different project though so I won't implement that soon
I'd also like somehow a list of the definition's abilities
These are abilities that an object of the definition can theoretically perform
This however is currently not a reasonable expectation
-------------------------------------------------------------------------------
If you have questions, suggestions, or ways to improve contact me:
My email is botahamec@outlook.com
"""

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

	def _get_definition_property_index(self, def_index, property):
		"""
		This function returns the index of a specific property of a definition
		This is meant to be used only for the webster object
		"""

		for index in range(0, len(self.dictionary[def_index].properties)):
			if list(self.dictionary[def_index].properties.keys())[index] == property:
				return index  # return the index of property with matching name
		raise Exception("No property of given name found")  # if none found

	def _get_object_property_index(self, object_index, property):
		"""
		This function returns the index of a specific property of an object
		This is meant to be used only for the webster object
		"""

		for index in range(0, len(self.memory[object_index].properties)):
			if list(self.memory[object_index].properties.keys())[index] == property:
				return index # return the index of property with matching name
		raise Exception("No property of given name found") # if none found

	def set_object_property(self, object, name, val):
		"""
		This function sets the value of a property for an object in memory
		If the property doesn't exist, then it is added
		"""

		self.memory[self._get_object_index(object)].properties[name] = val

	def set_definition_property(self, defn, name, val):
		"""
		This function the value of a property for a definition
		If the property doesn't exist it'll be added
		"""

		self.dictionary[self._get_definition_index(defn)].properties[name]=val

	def object_has_property(self, object, property):
		"""
		Returns true if the object has the property specified
		"""

		for key in self.get_object(object).properties.keys():
			if property == key: return True
		return False
	
	def definition_has_property(self, definition, property):
		"""
		Returns true if the definition has the property specified
		"""

		for key in self.get_definition(definition).properties.keys():
			if property == key: return True
		return False

	def object_has_definition(self, object, definition):
		"""
		Compares an object's properties with a definition's properties
		Returns true if the two are similar
		"""

		for name, value in definition.properties.items():
			if self.object_has_property(object, property):
				if value == None: continue
				elif self.get_object_property(object, name) == value: continue
				else: return False
			else: return False
		return True

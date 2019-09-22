import webster_py

# test Object.__init__()
def object_initialization():
	food = webster_py.Object("Food", {"Name": None,
								      "Group": None,
								      "Taste": None})
	print("Type: " + food.__class__.__name__)
	print("Name: " + food.name)
	print("Properties Type: " + food.properties.__class__.__name__)
	print("Properties:")
	for key, value in food.properties.items():
		print("    " + key + ": " + value.__class__.__name__)

# test Webster.__init__()
def webster_initialization():
	webster = webster_py.Webster()
	print("Webster Type: " + webster.__class__.__name__)
	print("Memory Type: " + webster.memory.__class__.__name__)
	print("Dictionary Type: " + webster.dictionary.__class__.__name__)
	print("Memory Length: " + str(len(webster.memory)))
	print("Dictionary Length: " + str(len(webster.memory)))

# test Webster.add_definition()
def definition_addition():
	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name" : None,
									"Group": None,
									"Taste": None})
	
	print("Dictionary Length: " + str(len(webster.dictionary)))
	print("Type: " + webster.dictionary[0].__class__.__name__)
	print("Name: " + webster.dictionary[0].name)
	print("Properties Type: " + webster.dictionary[0].properties.__class__.__name__)
	print("Properties:")
	for key, value in webster.dictionary[0].properties.items():
		print("    " + key + ": " + value.__class__.__name__)

# test Webster.get_definition()
def definition_fetch():
	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name" : None,
									"Group": None,
									"Taste": None})
	
	food = webster.get_definition("Food")
	print("Type: " + food.__class__.__name__)
	print("Name: " + food.name)
	print("Properties Type: " + food.properties.__class__.__name__)
	print("Properties:")
	for key, value in food.properties.items():
		print("    " + key + ": " + value.__class__.__name__)
	
	try: webster.get_definition("Money")
	except: print("An error returned, as expected")

	print("Dictionary Length: " + str(len(webster.dictionary)))

# test Webster.add_object()
def object_addition():
	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name" : None,
									"Group": None,
									"Taste": None})
	webster.add_object("0", "Food")
	print("Type: " + webster.memory[0].__class__.__name__)
	print("Name: " + webster.memory[0].name)
	print("Properties Type: " + webster.memory[0].properties.__class__.__name__)
	print("Properties:")
	for key, value in webster.memory[0].properties.items():
		print("    " + key + ": " + value.__class__.__name__)
	print("Memory Length: " + str(len(webster.memory)))

# test Webster.get_object()
def object_fetch():
	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name": None,
                                	"Group": None,
                                	"Taste": None})
	webster.add_object("0", "Food")
	food = webster.get_object("0")

	print("Type: " + food.__class__.__name__)
	print("Name: " + food.name)
	print("Properties Type: " + food.properties.__class__.__name__)
	print("Properties:")
	for key, value in food.properties.items():
		print("    " + key + ": " + value.__class__.__name__)
	print("Memory Length: " + str(len(webster.memory)))

# test Webster._get_definition_index()
def index_of_definitions():

	# populate the dictionary
	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name": None,
                                  	"Group": None,
                                  	"Taste": None})
	webster.add_definition("Color", {"General Name": None,
									 "Specfic Name": None,
									 "Red": None,
									 "Green": None,
									 "Blue": None,
									 "Hue": None,
									 "Saturation": None,
									 "Brightness": None})
	webster.add_definition("Number", {"Value": None,
									  "Spelling": None})

	food = webster._get_definition_index("Food")
	color = webster._get_definition_index("Color")
	number = webster._get_definition_index("Number")

	print("Food Index: " + str(food))
	print("Color Index: " + str(color))
	print("Number Index: " + str(number))

# test Webster._get_object_index()
def index_of_objects():

	# populate the dictionary
	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name": None,
                                 "Group": None,
                                 "Taste": None})
	webster.add_definition("Color", {"General Name": None,
                                  "Specfic Name": None,
                                  "Red": None,
                                  "Green": None,
                                  "Blue": None,
                                  "Hue": None,
                                  "Saturation": None,
                                  "Brightness": None})
	webster.add_definition("Number", {"Value": None,
                                   "Spelling": None})

	# populate the memory
	webster.add_object("Apple", "Food")
	webster.add_object("Cheese", "Food")
	webster.add_object("Carrot", "Food")
	webster.add_object("Red", "Color")
	webster.add_object("Green", "Color")
	webster.add_object("Purple", "Color")
	webster.add_object("1", "Number")
	webster.add_object("3", "Number")

	print("Apple Index: " + str(webster._get_object_index("Apple")))
	print("Cheese Index: " + str(webster._get_object_index("Cheese")))
	print("Carrot Index: " + str(webster._get_object_index("Carrot")))
	print("Red Index: " + str(webster._get_object_index("Red")))
	print("Green Index: " + str(webster._get_object_index("Green")))
	print("Purple Index: " + str(webster._get_object_index("Purple")))
	print("1 Index: " + str(webster._get_object_index("1")))
	print("3 Index: " + str(webster._get_object_index("3")))

# test Webster.get_definition_property()
def check_definition_properties():

	webster = webster_py.Webster()
	webster.add_definition("Apple", {"Name": "Apple",
                                  	 "Group": "Fruit",
									 "Taste": "Sweet",
									 "Species": None,
									 "Color": None})
	
	name = webster.get_definition_property("Apple", "Name")
	group = webster.get_definition_property("Apple", "Group")
	taste = webster.get_definition_property("Apple", "Taste")
	species = webster.get_definition_property("Apple", "Species")
	color = webster.get_definition_property("Apple", "Color")

	print("Name: " + name)
	print("Group: " + group)
	print("Taste: " + taste)
	print("Species: " + str(species))
	print("Color: " + str(color))

# test Webster.get_object_property()
def check_object_properties():

	webster = webster_py.Webster()
	webster.add_definition("Apple", {"Name": "Apple",
                                  	 "Group": "Fruit",
									 "Taste": "Sweet",
									 "Species": None,
									 "Color": None})
	webster.add_object("0", "Apple")

	name = webster.get_object_property("0", "Name")
	group = webster.get_object_property("0", "Group")
	taste = webster.get_object_property("0", "Taste")
	species = webster.get_object_property("0", "Species")
	color = webster.get_object_property("0", "Color")

	print("Name: " + name)
	print("Group: " + group)
	print("Taste: " + taste)
	print("Species: " + str(species))
	print("Color: " + str(color))

# test Webster.definition_of_type()
def definition_clone():

	webster = webster_py.Webster()
	webster.add_definition("Food", {"Name": None,
                                 "Group": None,
                                 "Taste": None})
	webster.definition_of_type("Apple", "Food")

	name = webster.get_definition_property("Apple", "Name")
	group = webster.get_definition_property("Apple", "Group")
	taste = webster.get_definition_property("Apple", "Taste")

	print("Name: " + str(name))
	print("Group: " + str(group))
	print("Taste: " + str(taste))
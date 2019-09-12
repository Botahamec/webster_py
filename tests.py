import webster_py

# test Object.__init__
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

# test Webster.__init__
def webster_initialization():
	webster = webster_py.Webster()
	print("Webster Type: " + webster.__class__.__name__)
	print("Memory Type: " + webster.memory.__class__.__name__)
	print("Dictionary Type: " + webster.dictionary.__class__.__name__)
	print("Memory Length: " + str(len(webster.memory)))
	print("Dictionary Length: " + str(len(webster.memory)))
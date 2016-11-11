import random

divider = "--------------------"

# The Count Function takes a list as a parameter, counts the 
# number of items in the list and returns the value
def count(aList):
	counter = 0
	for x in aList:
		counter+=1
	return counter

# The inFunction takes a list and a target as parameters, and checks to see 
# if the target is in the list. Returns true if found, otherwise it returns
# false
def inFunction(aList, target):
	for x in aList:
		if x == target:
			return True
	return False

# The reverse function takes a list as parameter, and reverses the order
# of the list and returns the reversed list
def reverse(aList):
	reverseList = []
	for x in aList:
		revNum = aList.index(x)
		negaVal = (1 + (revNum*2))
		reverseList.append(aList[revNum - negaVal])

	return reverseList

# The index function takes a list and a target as parameters, finds the index
# of the target inside the list and returns the index value
def index(aList, target):
	for x in range(len(aList)):
		if aList[x] == target:
			return x;
	return -1

# The insert function takes a list, a target and a position(number), creates a
# new list, inserts the target into the given position and returns a new list
def insert(aList, target, position):
	newList = []
	for x in range(len(aList)):
		if x == position:
			newList.append(target)
			newList.append(aList[x])
		else:
			newList.append(aList[x])
	return newList

#-------------------------------------------------------------------------------

if __name__ == "__main__":
	
	# Count Implementation
	#---------------------------------------------------------------------------
	# Created a list with varying sizes (0 to 20) with random values
	# between 0 and 1000
	print("\nCount Function\n" + divider)
	randListSize = random.randint(0, 20)
	myList = [random.randint(0,1000) for x in range(randListSize)]
	# Print list for visual purposes
	print(myList)
	# Call the function and store the value into the numOfItems variable
	numOfItems = count(myList)
	# Print out the number of items in the list.
	print(str(numOfItems) + " items in the list above.")
	#---------------------------------------------------------------------------
	# In Implementation
	# Create a fixed list this time
	print("\nIs_In Function\n" + divider)
	anotherList = ["Banana", "Eggs", "Potato", "Peppers", "Onions"]
	# Prints True
	print(inFunction(anotherList, "Eggs"))
	# Prints False
	print(inFunction(anotherList, "Beef"))

	# Reverse, Index and Insert Implementation
	print("\nReverse, Index and Insert\n" + divider)
	yetAnotherList = ["Ace", "Baboon", 5, True, "Wukong", "Plane"]
	print(reverse(yetAnotherList))
	print(index(yetAnotherList, True))
	print(insert(yetAnotherList, "Za Warudo", 4))

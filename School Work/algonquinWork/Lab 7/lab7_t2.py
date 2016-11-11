# Author: Windjy E. Jean
# Student #: 040875990

import sys

# Global Variables

divider = "--------------------"
listMsg = "Enter a list of values\n" + \
	"(Separate all values with a comma)"

# Mandatory Functions

def isSorted(aList):
	orderedList = []
	for x in aList:
		orderedList.append(x)
	orderedList.sort()
	# print("Original List: " + str(aList))
	# print("Ordered List: " + str(orderedList))
	return (orderedList == aList)

def isAnagram(firstWord, secondWord):
	listA = []
	listB = []

	firstWord = firstWord.lower()
	secondWord = secondWord.lower()

	# Takes care of whitespaces and insert all the characters
	# of a word in a list
	for x in range(len(firstWord)):
		if (firstWord[x] == " "):
			continue;
		else:
			listA.append(firstWord[x])

	for x in range(len(secondWord)):
		if (secondWord[x] == " "):
			continue;
		else:
			listB.append(secondWord[x])

	listA.sort()
	listB.sort()
	return (listA == listB)

def removeDuplicates(aList):
	distinct = []
	for x in aList:
		if x in distinct:
			continue;
		else:
			distinct.append(x)
	return distinct

def sumOfSquares(xs):
	total = 0;
	for x in xs:
		total += (float(x)**2)
	return total

# Add Modularity

def createList():
	theString4List = input()
	theList = theString4List.split(",")
	# print(theList)
	# Removes whitespaces and converts numbers
	# into integers types
	for x in range(len(theList)):
		theList[x] = theList[x].strip()
		if (theList[x].isdigit()):
			theList[x] = int(theList[x])

	return (theList)

def fetchExe(n):

	n = int(n)
	userList = []

	if (n == 1):
		print(listMsg)
		userList = createList()
		print(isSorted(userList))
		menu()
	elif (n == 2):
		print("Enter two words: ")
		wordOne = input("Word 1 --> ")
		wordTwo = input("Word 2 --> ")
		print(isAnagram(wordOne, wordTwo))
		menu()
	elif (n == 3):
		print(listMsg)
		userList = createList()
		print(removeDuplicates(userList))
		menu()
	elif (n == 4):
		print(listMsg)
		userList = createList()
		print(sumOfSquares(userList))
		menu()
	else:
		sys.exit()

def menu():
	print("\nSelect an exercise...\n" + divider)

	for i in range(1, 6):
		if (i == 1):
			print("1. Test isSorted")
		elif (i == 2):
			print("2. Test isAnagram")
		elif (i == 3):
			print("3. Test removeDuplicates")
		elif (i == 4):
			print("4. Test sumOfSquares")
		elif (i == 5):
			print("5. Exit")

	choice = input("--> ")
	while (int(choice) < 1 or int(choice) > 5):
		choice = input("--> ")

	fetchExe(choice)

if __name__ == '__main__':
	menu()
	# randList = [1, 2, 3, 2, 1]
	# # print(isSorted(randList))

	# # wordOne = "sett    ing"
	# # wordTwo = "te  sting"
	# # print(isAnagram(wordOne, wordTwo))
	# # print (removeDuplicates(randList))
	# squareList = [2, 3, 4]
	# print(sumOfSquares(squareList))

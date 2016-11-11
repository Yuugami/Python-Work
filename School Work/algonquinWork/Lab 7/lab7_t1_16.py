divider = "--------------------"

print("\n" + divider)
myList = [76, 92.3, "hello", True, 4, 76]
print("Original List: " + str(myList))
print(divider)

# Exercise A
print("\nExercise A")
print(divider)
myList.append("apple")
myList.append(76)
print("New List: " + str(myList))
print(divider)

# Exercise B
print("\nExercise B")
print(divider)
myList.insert(2, "cat")
print("New List: " + str(myList))
print(divider)

# Exercise C
print("\nExercise C")
print(divider)
myList.insert(0, 99)
print("New List: " + str(myList))
print(divider)

# Exercise D
print("\nExercise D")
print(divider)
print("Index of '" + myList[myList.index("hello")] + 
	"' in myList is " + str(myList.index("hello")))
print(divider)

# Exercise E
print("\nExercise E")
print(divider)
count = 0;

for x in myList:
	if (x == 76):
		count += 1

print("There are " + str(count) + " 76s");
print(divider)

# Exercise F
print("\nExercise F")
print(divider)

myList.remove(76)

print("Removed the first 76 in the list")
print("New list: " + str(myList))
print(divider)

# Exercise G
print("\nExercise G")
print(divider)

index = myList.index(True)
myList.pop(index)

print("Removed 'True' from list")
print("New list: " + str(myList))
print(divider)
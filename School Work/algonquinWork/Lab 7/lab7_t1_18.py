import random

def ex3(myList):
	maxValue = 0;
	for x in myList:
		if (x > maxValue):
			maxValue = x

	return(maxValue)

if __name__ == "__main__":
	myList = [random.randint(0,1000) for x in range(100)]
	# # To see list, uncomment code below
	# print(sorted(myList))
	maxValue = ex3(myList)
	print("\nThe max value is : " + str(maxValue))
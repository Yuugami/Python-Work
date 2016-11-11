"""
Lab 6 - More Functions

Author: Windjy E. Jean
Student #: 040875990
"""

import sys
divider = "--------------------"

def print_triangular_numbers(n):
	print("\nTriangular Numbers\n"+ divider)
	loopCont = 1
	while (loopCont <= n):
		part1 = loopCont * (loopCont + 1)
		ans = part1 / 2
		print(str(loopCont) + "    " + str(int(ans)))
		loopCont += 1

def myFactorial(n):
	print("\nFactorials\n" + divider)
	loopCont = 1
	ans = 1
	while (loopCont <= n):
		ans *= loopCont
		loopCont += 1

	return ans

def checkOddEven():
	print("\nCheck Odd Even\n" + divider)
	for i in range(21):
		if (i % 2 == 0):
			print (str(i) + " is even.")
		else:
			print (str(i) + " is odd.")

def printAsterisksV1(n):
	print("\nPrint Asterisks 1.0\n" + divider)
	print()
	for i in range(n):
		print ('*', end="")
	print()

def printAsterisksV2(n):
	print("\nPrint Asterisks 2.0\n" + divider)
	loopCont = 1
	while(loopCont in range(n+1)):
		print ('*')
		loopCont += 1

def printDiagonally(string):
	print("\nPrint Diagonally\n" + divider)
	lenOfString = len(string)
	for i in range(lenOfString):
		print(string[i])
		for index in range(i+1):
			print(" ", end="")

def fetchExe(n):

	n = int(n)

	if (n == 1):
		param = int(input("Calculating the triangular numbers. Choose a value: "))
		print_triangular_numbers(param)
		menu()
	elif (n == 2):
		param = int(input("Calculating factorial. Enter a number: "))
		ans = myFactorial(param)
		print("The factorial of " + str(param) + " is " + str(ans))
		menu()
	elif (n == 3):
		checkOddEven()
		menu()
	elif (n == 4):
		param = int(input("How many asterisks do you want to print: "))
		printAsterisksV1(param)
		menu()
	elif (n == 5):
		param = int(input("How many asterisks do you want to print: "))
		printAsterisksV2(param)
		menu()
	elif (n == 6):
		param = input("Enter a phrase: ")
		printDiagonally(param)
		menu()
	else:
		print("Exiting Program...")
		print("Thank you for testing my work.")
		sys.exit(0)


def menu():

	print("\nSelect an exercise...\n" + divider)

	for i in range(1, 8):
		if (i == 1):
			print("1. Test Exercise 2")
		elif (i == 2):
			print("2. Test myFactorial")
		elif (i == 3):
			print("3. Test checkOddEven")
		elif (i == 4):
			print("4. Test printAsterisksV1")
		elif (i == 5):
			print("5. Test printAsterisksV2")
		elif (i == 6):
			print("6. Test printDiagonally")
		else:
			print("7. Exit")

	choice = input("--> ")
	while (int(choice) < 1 or int(choice) > 7):
		choice = input("--> ")

	fetchExe(choice)


if __name__ == '__main__':
	menu()
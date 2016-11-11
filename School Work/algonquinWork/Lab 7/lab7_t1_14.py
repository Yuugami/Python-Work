divider = "--------------------"
spaces = " "

print("\n" + divider)
print("Before third line is executed...")
print(divider + "\n")
a = [1, 2, 3]
b = a[:]
print((spaces*5) + "A = " + str(a))
print((spaces*5) + "B = " + str(b) + "\n")
b[0] = 5;
print(divider)
print("After third line is executed...")
print(divider + "\n")
print((spaces*5) + "A = " + str(a))
print((spaces*5) + "B = " + str(b))
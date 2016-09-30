import math

def finalCompound (P, r, n, t):
	part1 = (r/n)
	part2 = 1 + part1
	part3 = part2 ** (n*t)
	part4 = P * part3
	return part4

principalAmount = 1820.40;
annualInterestRate = 0.08;
timesCompoundedPerYear = 12;

print("----------INFO-----------")
print("Principal Amount: $" + str(principalAmount));
print("Annual Interest Rate: " + str(annualInterestRate) + "%");
print("# of Times Interest is Compounded Per Year: " + 
	str(timesCompoundedPerYear));
print("-------------------------");
numberOfYears = int(input("Enter the number of years the principal " +
	"is compounded for: "))

finalAmt = finalCompound(principalAmount, annualInterestRate,
	timesCompoundedPerYear, numberOfYears);

finalAmt = round(finalAmt, 2)

print("Final Amount after " + str(numberOfYears) + " years is: $" + str(finalAmt));
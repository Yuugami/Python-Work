########################################################### 
#          Canadian Postal Code Checker
#          ----------------------------
#
#            Author: Windjy E. Jean
#             Student#: 040875990
# K1R 5M5
# 012 345
###########################################################

import sys
divider = "-----------------------"

def validatePCode (pCode):
	print("\nPostal Code Entered: " + pCode);
	print(divider);

	if (not postalCodeMap(pCode[0])):
		return False
	
	if (len(pCode) != 6):
		return False

	for i in range(len(pCode)):
		if (pCode[i].isdigit()):
			if (i % 2 == 0):
				return False
		else:
			if (i % 2 != 0):
				return False

	return True

def requestPCode():
	print("Enter a Valid Postal Code: ");
	pCode = input("--> ").upper().replace(" ", "");
	valid = validatePCode(pCode);

	if valid:
		return pCode;
	else:
		print("Invalid Postal Code");
		sys.exit();

def postalCodeMap(firstChar):

	postalCodeMap.codeDefinition = {
	"A" : "Newfoundland",
	"B" : "Nova Scotia",
	"C" : "Prince Edward Island",
	"E" : "New Brunswick",
	"G" : "Quebec",
	"H" : "Quebec",
	"J" : "Quebec",
	"K" : "Ontario",
	"L" : "Ontario",
	"M" : "Ontario", 
	"N" : "Ontario", 
	"P" : "Ontario",
	"R" : "Manitoba",
	"S" : "Saskatchewan",
	"T" : "Alberta",
	"V" : "British Columbia",
	"X" : "Nunavut or Northwest Territories",
	"Y" : "Yukon"};

	if (firstChar in postalCodeMap.codeDefinition):
		return True;
	else:
		return False;

if __name__ == "__main__":
	postalCode = requestPCode();

	if (postalCode[1] == "0"):
		typeAdr = "Rural"
	else:
		typeAdr = "Urban"

	print("Province: " + postalCodeMap.codeDefinition[postalCode[0]]);
	print("Address Type: " + typeAdr);
def mpg(a, b):
    mpg = a / b;
    mpg = round(mpg, 3);
    return mpg;

miles = float(input("Enter the number of miles driven: "));
gallons = float(input("Enter the number of gallons used: "));

mpg = mpg(miles, gallons);
print ("Your vehicle can go " + str(mpg) + " miles per gallon.");

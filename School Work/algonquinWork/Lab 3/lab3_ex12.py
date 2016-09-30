def fahToCelsius(f):
    part1 = f - 32;
    part2 = 9.0/5.0
    part3 = part1 / part2;
    part3 = round(part3, 2)
    return part3;

fahrenheit = input("Input a value for degrees fahrenheit: ");
fahrenheit = float(fahrenheit);
celsius = fahToCelsius(fahrenheit);

print ("---------------------");
print ("Fahrenheit: " + str(fahrenheit) + "F");
print ("Celsius: " + str(celsius) + "C");

import math

def areaOfCircle(radius):
    area = (radius**2) * math.pi;
    return area;

print ("Computing area of a circle. Please enter the radius.");
radius = int(input("-->"));

area = areaOfCircle(radius);

print ("The area of your circle is: " + str(area));

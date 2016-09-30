import math

def calcDist(p1, p2):
	deltaX = p2[0] - p1[0];
	deltaY = p2[1] - p1[1];
	
	deltaX2 = deltaX ** 2;
	deltaY2 = deltaY ** 2;

	part3 = deltaX2 + deltaY2;

	distance = math.sqrt(part3);
	return distance;

# P1 - Point 1
# P2 - Point 2
# Both variables will be array that contain X and Y coordinate.
p1 = [0, 0];
p2 = [10, 50];

dist = calcDist(p1, p2);

divider = "----------------------"
print(divider);
print("Point 1 Coordinates: (" + str(p1[0]) + ", " + str(p1[1]) + ")");
print("Point 2 Coordinates: (" + str(p2[0]) + ", " + str(p2[1]) + ")");
print(divider);
print("The distance between both coordinates is: " + str(round(dist, 3)));
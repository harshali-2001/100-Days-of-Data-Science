import math

def area(r):
    return math.pi * r*r

radius = int(input("Enter radius of a circle : "))

print("Area of a circle is " , area(radius))

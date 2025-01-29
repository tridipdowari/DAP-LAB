import math

def circleArea(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = circleArea(radius)
print(f"The area of the circle with radius {radius} is {area}")
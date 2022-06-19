import math


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def rightTrianglePerimeter(a, b):
    return hypotenuse(a, b) + a + b

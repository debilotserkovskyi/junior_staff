import math


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def distance2D(x1, y1, x2, y2):
    return hypotenuse(a=x1-x2, b=y1-y2)
